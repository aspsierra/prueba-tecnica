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
        let searchFilters = this.formatQueryParams(params); 
        let res = await this.getQuery(this.baseApiUrl + 'tasks-list/', searchFilters)
        
        return res
    }

    formatQueryParams(params) {
        let searchFilters = {}
        for (const [key, value] of Object.entries(params)) {
            
            if (key === "due_date"){
                for (const [dateKey, dateValue] of Object.entries(value)) {
                    if(dateValue){
                        searchFilters[`${key}_${dateKey}`] = dateValue;
                    }
                }
            } else if (value) {
                searchFilters[key] = value;
            }
        }

        return searchFilters
    }

    async getFamilies(){
        return await this.getQuery(this.baseApiUrl + 'families/')
    }

    async getStates() {
        let states = await this.getQuery(this.baseApiUrl + 'task-states/')
        
        let formattedStates = []
        for (const state of states){
            formattedStates.push(
                {id: state.value, name: state.label}
            )
        } 

        return formattedStates
        
    }
}