import axios from "axios";
// axios is a clean way to send network request;
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
});

api.interceptors.request.use(
    (config) => {
         const token = localStorage.getItem(ACCESS_TOKEN);
         if (token) {
            config.headers.Authorization = 'Bearer ${token}';
         }
         return config;
    },
    (error) => {
        return Promise.reject(error);
    }
)
export default api;