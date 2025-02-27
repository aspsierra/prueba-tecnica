import axios from "axios";

export class Api {
    headers = {'Content-Type': 'application/json'}
    baseApiUrl = import.meta.env.VITE_API_URL

    async getQuery(URL, searchParams={}, headers=this.headers){

        return await axios
            .get(URL, { 
                headers: headers,
                params: searchParams
            })
            .then(response => response.data)
            .catch(err => {
                console.error('GET request failed:', err);
                throw err
            })
    }

    async getAllTasks(params={}){
        let searchFilters = {}

        for (const [key, value] of Object.entries(params)){
            if(value){
                searchFilters[key] = value
            }    
        } 

        let res = await this.getQuery(this.baseApiUrl + 'tasks-list', searchFilters)
        
        return res
    }

    async getFamilies(){
        return await this.getQuery(this.baseApiUrl + 'families/')
    }
}