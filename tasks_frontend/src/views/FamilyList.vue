<template>
    <main class="container px-40 pt-20 pb-10">
        <header class="flex justify-between mb-5">
            <h1 class="text-3xl text-white font-bold mb-5">Listado de Familias</h1>
            <RouterLink @click="openModal" class="btn btn-active btn-primary">
                <Icon icon="material-symbols:add-2-rounded" width="24" height="24" />
                Añadir familia
            </RouterLink>
        </header>

        <FamilyListFilters
            :filters="filters"
            :resetFilters="resetFilters"
            :ordering="ordering"
            @order="orderTable"
        />

        <div class="mt-5">
            <div >
                <div v-for="family in families" class="cursor-pointer border-gray-500 hover:brightness-75 border-b-2 mb-2">      
                    <RouterLink :to="`/family/${family.id}`">
                        <FamilyOverview :family="family"/>
                    </RouterLink>
                </div>
            </div>
        </div>
        
    </main>

</template>


<script>
import FamilyOverview from '@/components/FamilyOverview.vue';
import FamilyListFilters from '@/components/filters/FamilyListFilters.vue';
import { useStore } from '@/stores/store';
import { Icon } from '@iconify/vue';
import _ from 'lodash';
import { mapActions, mapState } from 'pinia';
import { RouterLink } from 'vue-router';


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
        FamilyListFilters,
        Icon
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