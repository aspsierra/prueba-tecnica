import { useStore } from "@/stores/store";
import axios from "axios";

export class Api {
    headers = {'Content-Type': 'application/json'}
    baseApiUrl = import.meta.env.VITE_API_URL

    getAuthHeaders() {
        const store = useStore()
        const token = store.token;
        return token ? { ...this.headers, Authorization: `Bearer ${token}` } : this.headers;
    }

    async getQuery(URL, searchParams={}, headers=this.getAuthHeaders()){

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

    async postQuery(URL, data, headers=this.getAuthHeaders()) {
        return axios    
            .post(URL, data, {headers : headers})
            .then(response => response.data)
            .catch(err => {
                console.error('POST request failed', err)
                throw err
            })
    }

    async putQuery(URL, data, headers=this.getAuthHeaders()){
        return await axios
            .put(URL, data, {headers : headers})
            .then(response => true)
            .catch(err => {
                console.error('PUT request failed', err)
                throw err
            })
    }

    async deleteQuery(URL, headers=this.getAuthHeaders()){
        return await axios
            .delete(URL, {headers : headers})
            .then(response => true)
            .catch(err => {
                console.error('DELETE request failed', err)
                throw err
            })
    }

    formatQueryParams(params, order) {
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

        if (order) {
            searchFilters['ordering'] = order
        }

        return searchFilters
    }

    async getAllTasks(params={}, ordering = ''){
        let searchFilters = this.formatQueryParams(params, ordering); 
        let res = await this.getQuery(this.baseApiUrl + 'tasks-list/', searchFilters)
        
        return res
    }

    async getFamilies(params={}, ordering = ''){
        return await this.getQuery(this.baseApiUrl + 'families/', this.formatQueryParams(params, ordering))
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
    
    async getTaskData(id){
        return await this.getQuery(this.baseApiUrl + `task-detail/${id}`)
    }

    async updateTask(data){
        return await this.putQuery(this.baseApiUrl + `task-detail/${data.id}/update/`, data)
    }

    async deleteTask(id) {
        return await this.deleteQuery(this.baseApiUrl + `task-detail/${id}/delete/`)
    }

    async addTask(data){
        console.log(data);
        
        return await this.postQuery(this.baseApiUrl + 'task-detail/create-task/', data)
    }

    async getUserToken(data){
        return await this.postQuery(this.baseApiUrl + 'token/', data)
    }

    async getUserData(){
        return await this.getQuery(this.baseApiUrl + 'auth/user/')
    }

    async logout(){
        return await this.postQuery(this.baseApiUrl + 'auth/logout/', {})
    }
}