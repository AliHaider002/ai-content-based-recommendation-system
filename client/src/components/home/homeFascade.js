import moviesService from "../../utils/controllers/moviesServices";

export const getMovies = async (id) => {
  try {
    const resp = await moviesService.fetchPopularMovies(id);
    return resp;
  } catch (error) {
    console.log("error: ", error);
  }
};

export const getRecommendations = async (title = "") => {
  try {
    const resp = await moviesService.fetchRecommendedMovies(title);
    return resp;
  } catch (error) {
    console.log("error: ", error);
  }
};
