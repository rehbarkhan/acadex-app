<script setup>
import { useDesignationGetList } from '@/services/designation';
import NewDesignation from '@/components/hr/NewDesignation.vue';
import moment from 'moment';
import { Column, DataTable, Tag, IconField, InputIcon, InputText, Button} from 'primevue';
import { onMounted } from 'vue';
import { ref } from 'vue';
const {loading, error, first, data, getList, onPage, pageNumber, name_search, filter} = useDesignationGetList();
onMounted(async() => await getList())

async function reFetch(){
    pageNumber.value = 1;
    first.value = 0;
    name_search.value = ''
    await getList()
}

function cool(data){
}

</script>
<template>
    <div class="flex w-full justify-between items-center my-7">
        <div class="text-xl font-semibold">Designation</div>
        <div><NewDesignation @recordCreated="reFetch" /></div>
    </div>
    <!-- <input type="text" v-model="name_search" @keydown.enter="filter" /> -->
    <IconField class="mb-5">
        <InputIcon class="pi pi-search" />
        <InputText v-model="name_search" @keydown.enter="filter" placeholder="Search" fluid="" size="small"/>
    </IconField>
    <DataTable 
        size="small"
        :value="data.results"
        :loading="loading"
        :first="first"
        stripedRows
        tableStyle="min-width: 50rem"
        paginator
        :totalRecords="data.count"
        @page="onPage"
        :rows="10"
        lazy
        >
        <template #header> In total there are {{ data.count }} designation records </template>
        <Column field="id" header="#ID"></Column>
        <Column header="Created">
            <template #body="slotProps">
                {{ moment(slotProps.data.created).format('MMMM Do YYYY, h:mm:ss a')}}
            </template>
        </Column>
        <Column field="name" header="Designation Name"></Column>
        <Column header="Status">
            <template #body="slotProps">
                <Tag v-if="slotProps.data.is_agedout" severity="danger" value="Not Active"></Tag>
                <Tag v-else severity="success" value="Active"></Tag>
            </template>
        </Column>
        <Column header="Action">
            <template #body="slotProps">
                <Button label="View" icon="pi pi-pencil" :size="small" @click="()=>cool(slotProps.data)" />
            </template>
        </Column>
        
    </DataTable>

</template>

