
<script setup>
import { Button, IconField, InputIcon, InputText } from 'primevue';
import { useLogin } from '@/services/auth/login';
import { ref } from 'vue';


const {loading, error, login} = useLogin();
const cred = ref({username: '', password: ''})
const triggerLogin = async () => {
    await login(cred.value.username, cred.value.password);
}

</script>

<template>
    Login
    <div v-show="error" class="font-bold text-red-600">
        Kindly correct your login credential
    </div>
    <form @submit.prevent="triggerLogin">
        <div>
            <IconField>
                    <InputIcon class="pi pi-user" />
                    <InputText placeholder="johndoe" v-model="cred.username" required autofocus/>
            </IconField>
            <IconField>
                    <InputIcon class="pi pi-user" />
                    <InputText type='password' placeholder="password" v-model="cred.password" required />
            </IconField>
            <Button label="Login" type="submit" :loading="loading" />
        </div>
    </form>
</template>