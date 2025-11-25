import axios from "axios";

const apiPublic = axios.create({
  baseURL: "/api",
  withCredentials: true  // чи відправляти cookies
});

export default apiPublic;
