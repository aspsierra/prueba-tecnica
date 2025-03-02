import { defineStore } from "pinia";
import { Api } from "@/services/api";
import _ from 'lodash'

export const useStore = defineStore('main', {
    state: () => ({
        families: [],
        states: [],
        tasks: [],
        task: {
            // "due_date": ""        
        },
        api: new Api(),
        fromRoute: "/",
        token: null,
        user: {}
    }),
    actions: {
        setFromRoute(route){
            this.fromRoute = route
        },
        resetTask() {
            this.task = {
                // "due_date": ""        
            }
        },
        async setFamilies(params={}, ordering = ''){
            this.families = await this.api.getFamilies(params, ordering)
        },
        async setStates(){
            this.states = await this.api.getStates()
        },
        async setTasks(params={}, ordering='') {
            console.trace()
            this.tasks = await this.api.getAllTasks(params, ordering)
        },
        async filterTasks(filters, order){
            const debounceFilter = _.debounce(async () => {
                await this.setTasks(filters, order)
            }, 300)

            await debounceFilter(filters, order)
        },
        async filterFamilies(filters, order){
            const debounceFilter = _.debounce(async () => {
                await this.setFamilies(filters, order)
            }, 300)

            await debounceFilter(filters, order)
        },
        async getTaskDetails(id){
            this.task = await this.api.getTaskData(id)
        },

        async updateTaskDetails(data){
            return await this.api.updateTask(data)
        },
        async deleteSelectedTask(id = this.task.id){
            console.log('en store');    
            let res = await this.api.deleteTask(id)
            this.tasks = this.tasks.filter(task => task.id !== id);
            return res
        },
        async addNewTask(data){
            this.task = await this.api.addTask(data)
        },

        async getUser(newToken){
            this.token = newToken
            localStorage.setItem('token', newToken);
            this.user = await this.api.getUserData()
        },

        async logout(){
            await this.api.logout()
            this.user = {}
            this.token = null
            localStorage.removeItem('token')
        }


    }
})