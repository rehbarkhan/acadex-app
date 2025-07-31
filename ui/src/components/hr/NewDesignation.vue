<script setup>
import { ref } from "vue";
import { Button, Dialog, InputText , Message, useToast} from "primevue";
import { useDesignationCreate } from "@/services/designation";

const toast = useToast();
const {loading, error, name, error_msg,  createDesignation } = useDesignationCreate();
const emit = defineEmits(['recordCreated']);
const visible = ref(false);
async function createRecord(){
    await createDesignation();
    if(!error.value){
        emit('recordCreated');
        visible.value = false;
        toast.add({ severity: 'success', summary: 'Added Designation', detail: 'Successfully register designation', life: 3000 });
    }
}

</script>
<template>
   
        <Button label="Designation" icon="pi pi-plus" @click="visible = true" size="small"/>
        <Dialog v-model:visible="visible" modal header="New Designation" :style="{ width: '25rem' }">
            <form @submit.prevent="createRecord">
                <div v-show="error" class="my-3">
                    <Message severity="error"> {{ error_msg }}</Message>
                </div>
                <div class="flex flex-col  gap-4 mb-4">
                    <label for="username" class="font-semibold">Designation Name</label>
                    <InputText id="username" v-model="name" class="flex-auto" autocomplete="off" size="small"/>
                </div>
                <!-- <div class="flex items-center gap-4 mb-8">
                    <label for="email" class="font-semibold w-24">Email</label>
                    <InputText id="email" class="flex-auto" autocomplete="off" />
                </div> -->
                <div class="flex justify-end gap-2">
                    <Button type="button" label="Cancel" :loading="loading" severity="secondary" @click="visible = false" size="small"></Button>
                    <Button type="submit" label="Save" :loading="loading" size="small"></Button>
                </div>
            </form>
        </Dialog>
   
</template>


