import axios from "axios";

export class Api {
    headers = {'Content-Type': 'application/json'}
    baseApiUrl = import.meta.env.VITE_API_URL

    async get(URL, headers=this.headers, searchParams){
        return await axios.get(URL, { headers, params: searchParams})
            .then(response => response.data)
            .catch(err => {
                console.error('GET request failed:', err);
                throw err
            })
    }

    async getAllTasks(params={}){
        console.log(params);
        let searchFilters = {}

        for (const [key, value] of Object.entries(params)){
            console.log(key, value);
            if(value){
                searchFilters[key] = value
            }    
        } 

        console.log(searchFilters);
        
        
        return await this.get(this.baseApiUrl + 'tasks-list/', searchFilters)
    }

    async getFamilies(){
        return await this.get(this.baseApiUrl + 'families/')
    }
}