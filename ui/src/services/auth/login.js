import { useRoute } from "vue-router";
import axios from "axios";
import { ref } from "vue";

export function useLogin(){
    const loading = ref(false);
    const error = ref(false);
    const route = useRoute();
    async function login(username, password){
        loading.value = true;
        try{
            await axios.post('/api/Login/', {username, password});
            const next = route.query.next || false
            if (next){
                window.location.href = next;
            }else{
                window.location.href = "/"
            }
        }catch(E){
            error.value = true;
        }finally{
            loading.value = false;
        }
    }
    return {
        loading, error , login
    }
}