import axios from "axios";
import { ref } from "vue";

export function useDesignationGetList(){
    const loading = ref(false);
    const name_search = ref('');
    const error = ref(false);
    const data = ref({});
    const first = ref(0);
    const pageNumber = ref(1);
    async function getList(){

        loading.value = true;
        error.value = false;
        try{
            const response = await axios.get(`/api/Designation/?page=${pageNumber.value}&name__icontains=${name_search.value}`);
            data.value = response.data;
        }catch(E){
            error.value = true;
        }finally{
            loading.value = false;
        }
    }
    
    function onPage(event){
        pageNumber.value = event.page + 1;
        first.value = event.first;
        getList();
    }

    function filter(){
        pageNumber.value = 1;
        first.value = 0; 
        getList();
    }

    return {
        loading,
        error,
        data,
        name_search,
        first,
        pageNumber,
        onPage,
        getList,
        filter
    }
}


export function useDesignationCreate(){
    const loading = ref(false);
    const error = ref(false);
    const name = ref('');
    const error_msg = ref('');
    async function createDesignation(){
        loading.value = true;
        error.value = false;
        error_msg.value = '';
        try{
            await axios.post('/api/Designation/', {name: name.value});
            
        }catch(E){
            error.value = true;
            const response = E?.response?.data;

            // Handle validation error or detail error
            if (response?.detail) {
                error_msg.value = response.detail;
            } else if (response?.name?.length > 0) {
                error_msg.value = response.name[0];  // First validation message for 'name'
            } else {
                error_msg.value = "An unexpected error occurred.";
            }
        }finally{
            loading.value = false;
        }
    }
    return {
        loading, error, name , createDesignation, error_msg
    }
}


