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
import { useStore } from '@/stores/store';
import _ from 'lodash';
import { mapActions, mapState } from 'pinia';


export default {
    data(){
        return {
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
    computed: {
        ...mapState(useStore, ['families']),
    },
    watch: {
        filters: {
            handler: function(newFilters) {
                this.filterFamilies(newFilters, this.ordering)
            },
            deep: true
        }
    },
    methods: {
        ...mapActions(useStore, ['filterFamilies', 'setFamilies']),
        async orderTable(orderBy){
            this.ordering= orderBy 
            await this.setFamilies(this.filters, this.ordering)
        }
    },
    mounted() {
        this.setFamilies({}, 'name')
    }

}

</script>