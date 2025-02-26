import axios from "axios";

export class Api {
    headers = {'Content-Type': 'application/json'}
    baseApiUrl = import.meta.env.VITE_API_URL

    async get(URL, headers=this.headers){
        return await axios.get(URL, {headers})
            .then(response => response.data)
            .catch(err => {
                console.error('GET request failed:', err);
                throw err
            })
    }

    async getAllTasks(){
        return await this.get(this.baseApiUrl + 'tasks-list')
    }
}