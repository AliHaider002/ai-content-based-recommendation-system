import axios from "axios";
import { base_url } from "./baseUrl";

const onSuccess = (response) => {
  console.debug("Request Successful!", response);
  return response;
};

const onError = async (error) => {
  console.debug("Request Failed:", error);

  console.debug("Request Failed:", error.config);

  if (error?.response?.status === 401) {
    window.location.href = "/";
  }
  console.debug("Status:", error?.response?.status);
  console.debug("Data:", error?.response?.data);
  console.debug("Headers:", error?.response?.headers);

  return Promise.reject({
    error: error?.response?.data?.error || error?.response?.data,
    status: error?.response?.status,
  });
};

const request = async (options) => {
  let headers = {};

  // let authToken = JSON.parse(Cookies.get("user"))?.jwToken;
  // headers["Authorization"] = `Bearer ${Cookies.get("user") ? authToken : ""}`;
  const client = axios.create({
    baseURL: base_url,
    headers: { ...headers },
  });

  return client(options).then(onSuccess).catch(onError);
};
export default class BaseService {
  static get = (url, data) => {
    return request({
      url,
      method: "GET",
      data,
    });
  };
  static delete = (url, data) => {
    return request({
      url,
      method: "DELETE",
      data,
    });
  };

  static post = (url, data) => {
    return request({
      url,
      method: "POST",
      data,
    });
  };

  static put = (url, data) => {
    return request({
      url,
      method: "PUT",
      data,
    });
  };

  static extenralAPICall = (url) => {
    const client = axios({
      url,
      method: "GET",
      timeout: 1000 * 3,
    });
    return client.then(onSuccess).catch(onError);
  };
}
