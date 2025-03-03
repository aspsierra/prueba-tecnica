<template>
    <main v-if="!register" class="m-10 mt-2">
        <h3 class="my-5  text-xl font-bold">Iniciar Sesión</h3>
        <form @submit.prevent="login">

            <label class="form-control my-4">
                <div v-if="formError.username" class="label">
                    <span class="label-text font-normal text-red-500"> {{ formError.username[0] }} </span>
                </div>
                <TextInput class="w-full" :class="formError.username ? 'input-error' : ''" v-model="user.username"
                    label="Usuario" />
            </label>
            <label class="form-control  my-4">
                <div v-if="formError.password" class="label">
                    <span class="label-text font-normal text-red-500"> {{ formError.password[0] }} </span>
                </div>
                <PasswordInput :class="formError.password ? 'input-error' : ''" v-model="user.password" label="Contraseña" />

            </label>

            <p class="text-red-500" v-if="formError.detail">{{ formError.detail }}</p>


            <div class="w-full text-center">
                <p @click="changeForm" class="text-info hover:cursor-pointer">Regístrate</p>
            </div>


            <div class="w-full text-right mt-5">
                <div @click="loginGithub" class="btn btn-md btn-info">
                    <Icon icon="material-symbols:check-rounded" width="24" height="24" />
                    Iniciar con github
                </div>

                <div @click="loginUser" class="btn btn-md btn-info">
                    <Icon icon="material-symbols:check-rounded" width="24" height="24" />
                    Iniciar Sesión
                </div>
            </div>
        </form>
    </main>

    <main v-if="register" class="m-10 mt-2">
        <h3 class="my-5  text-xl font-bold">Registro</h3>
        <form @submit.prevent="login">

            <label class="form-control my-4">
                <div v-if="formError.username" class="label">
                    <span class="label-text font-normal text-red-500"> {{ formError.username[0] }} </span>
                </div>
                <TextInput class="w-full" :class="formError.username ? 'input-error' : ''" v-model="registerUser.username"
                    label="Usuario" />
            </label>
            <label class="form-control  my-4">
                <div v-if="formError.password1" class="label">
                    <span class="label-text font-normal text-red-500"> {{ formError.password1[0] }} </span>
                </div>
                <PasswordInput :class="formError.password1 ? 'input-error' : ''" v-model="registerUser.password1" label="Contraseña" />

            </label>

            <label class="form-control  my-4">
                <div v-if="formError.password2" class="label">
                    <span class="label-text font-normal text-red-500"> {{ formError.password2[0] }} </span>
                </div>
                <PasswordInput :class="formError.password2 ? 'input-error' : ''" v-model="registerUser.password2" label="Repite contraseña" />

            </label>

            <p class="text-red-500" v-if="formError.detail">{{ formError.detail }}</p>
            <p class="text-red-500" v-if="formError.non_field_errors">{{ formError.non_field_errors[0] }}</p>


            <div class="w-full text-center mt-2">
                <p @click="changeForm" class="text-info hover:cursor-pointer">Inicia sesión</p>
            </div>


            <div class="w-full text-right mt-5">

                <div @click="registerUserData" class="btn btn-md btn-info">
                    <Icon icon="material-symbols:check-rounded" width="24" height="24" />
                    Regístrate
                </div>
            </div>
        </form>
    </main>
</template>

<script>
import PasswordInput from '@/components/inputs/PasswordInput.vue';
import TextInput from '@/components/inputs/TextInput.vue';
import { useStore } from '@/stores/store';
import { Icon } from '@iconify/vue';
import { mapActions } from 'pinia';

export default {
    data() {
        return {
            user: {
                username: '',
                password: '',
            },
            registerUser: {
                username: '',
                password1: '',
                password2: '',
            },
            error: null,
            formError: {},
            register: false,
        };
    },
    components: {
        TextInput,
        PasswordInput,
        Icon
    },
    methods: {
        ...mapActions(useStore, ['login']),
        async loginUser() {
            try {
                let response = await this.$api.getUserToken(this.user)
                console.log(response);     
                await this.login(response.access)
                this.formError = {}
                this.$emit('closeForm')
            } catch (err) {
                console.log(err);
                
                this.formError = err.response.data
            }
        },
        changeForm(){
            this.register = !this.register
            this.formError = {} 
        },
        async registerUserData() {
            try {
                let response = await this.$api.register(this.registerUser)
                this.user = {
                    username: this.registerUser.username,
                    password: this.registerUser.password1
                }
                console.log(this.user);  
                this.loginUser()  

            } catch (err) {
                console.log(err);
                
                this.formError = err.response.data
            }
        },
        async loginGithub(){
            await this.$auth.loginWithGitHub()
        }
    }
};
</script>