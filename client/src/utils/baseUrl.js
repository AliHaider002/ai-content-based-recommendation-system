export const base_url =
  import.meta.env.VITE_STATUS === "development"
    ? import.meta.env.VITE_LOCAL_BASEURL
    : import.meta.env.VITE_SERVER_BASEURL;

export const VISITOR_TOKEN = import.meta.env.VITE_VISITOR_TOKEN;

export const uploads_uri =
  import.meta.env.VITE_STATUS === "development"
    ? import.meta.env.VITE_LOCAL_BASEURL_IMAGE
    : import.meta.env.VITE_SERVER_BASEURL_IMAGE;
