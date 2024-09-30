import React, { useEffect, useState } from "react";
import { getMovies } from "./homeFascade";
import { TMDB_IMAGE_PATH } from "../../utils/constants";
import Recommend from "./recommend";

const HomeCom = () => {
  const [page, setPage] = useState(1);
  const [data, setData] = useState([]);
  const [title, setTitle] = useState("");

  const fetchAllMovies = async () => {
    try {
      const resp = await getMovies(page);

      if (resp && resp.results && resp.results.length > 0) {
        setData(resp.results);
      }
    } catch (error) {
      console.log("error: ", error);
    }
  };
  useEffect(() => {
    fetchAllMovies();
  }, []);
  return (
    <div>
      <Recommend title={title} />
      <div className="grid grid-cols-5 gap-[2rem] items-center">
        {" "}
        {data &&
          data.length > 0 &&
          data.map((v, i) => {
            return (
              <div key={i} className="flex flex-col justify-normal gap-[1rem]">
                <div>
                  <img
                    src={TMDB_IMAGE_PATH + v.poster_path}
                    alt={v.original_title}
                  />
                </div>
                <div className="flex justify-between items-center">
                  <div>{v.release_date}</div>
                  <div>{v.original_language}</div>
                </div>
                <div className="flex justify-between items-center gap-[0.5rem]">
                  <div
                    onClick={() => setTitle(v.original_title)}
                    className="text-[1.2rem] font-bold cursor-pointer border-b border-transparent hover:border-white/60 transition-all duration-500"
                  >
                    {v.original_title}
                  </div>
                  <div className="text-[0.875rem] font-bold text-yellow-500 ">
                    {v.vote_average}
                  </div>
                </div>
                <div className="text-[1rem] line-clamp-3">{v.overview}</div>
              </div>
            );
          })}
      </div>
    </div>
  );
};

export default HomeCom;
