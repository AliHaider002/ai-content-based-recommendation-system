import ApiInstance from "../axiosconfig";
import { GET_ALL_Movies, GET_ALL_Recommendations } from "../routes";

const fetchPopularMovies = async (id = 1) => {
  const response = await ApiInstance.get(GET_ALL_Movies(id));
  return response.data;
};

const fetchRecommendedMovies = async (title = "") => {
  const data = {
    title: "Avatar",
  };
  const response = await ApiInstance.post(GET_ALL_Recommendations, data);
  return response.data;
};

const moviesService = {
  fetchPopularMovies,
  fetchRecommendedMovies,
};

export default moviesService;
