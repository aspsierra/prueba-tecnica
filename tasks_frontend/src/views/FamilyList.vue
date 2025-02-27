<template>
    <main class="container px-40 pt-20 pb-10">
        <h1 class="text-3xl text-white font-bold mb-5">Listado de Familias</h1>

        <FamilyListFilters
            :filters="filters"
            :resetFilters="resetFilters"
            :ordering="ordering"
            @order="orderTable"
        />

        <div class="mt-5">
            <div >
                <div v-for="family in families" class="cursor-pointer border-gray-500 hover:brightness-75 border-b-2 mb-2">      
                    <FamilyOverview :family="family"/>
                </div>
            </div>
        </div>
        
    </main>

</template>


<script>
import FamilyOverview from '@/components/FamilyOverview.vue';
import FamilyListFilters from '@/components/filters/FamilyListFilters.vue';
import _ from 'lodash';


export default {
    data(){
        return {
            families: [],
            filters: {
                name: '',
            },
            resetFilters: {
                name: '',
            },
            ordering: 'name'
        }
    },
    components: {
        FamilyOverview,
        FamilyListFilters
    },
    watch: {
        filters: {
            handler: _.debounce(async function (newFilters) {
                await this.fetchFamilies(newFilters, this.ordering)
            }, 300),
            deep: true
        }
    },
    async mounted(){
        await this.fetchFamilies()
    },
    methods: {
        async fetchFamilies(filters=this.filters, order=this.ordering){
            this.families = await this.$api.getFamilies(filters, order)
        },
        async orderTable(orderBy){
            this.ordering= orderBy 
            await this.fetchFamilies()
            
        }
    }

}

</script>