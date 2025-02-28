import { defineStore } from "pinia";
import { Api } from "@/services/api";
import _ from 'lodash'

export const useStore = defineStore('main', {
    state: () => ({
        families: [],
        states: [],
        tasks: [],
        task: {},
        api: new Api()
    }),
    actions: {
        async setFamilies(params={}, ordering = ''){
            this.families = await this.api.getFamilies(params, ordering)
        },
        async setStates(){
            this.states = await this.api.getStates()
        },
        async setTasks(params={}, ordering = '') {
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
            this.task = await this.api.getTaskDetails(id)
            this.task.due_date = this.formatDate(this.task.due_date)
        },
        formatDate(date){
            return new Intl.DateTimeFormat("es-ES",{
                day: "2-digit",
                month: "2-digit",
                year:"numeric"
              }).format(new Date(date))
        
        }
    }
})