<template>
    <main class="m-10 mt-2">
        <h3 class="my-5  text-xl font-bold text-white">Iniciar Sesión</h3>
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

            <div class="w-full text-right mt-5">

                <div v-if="!newTask" @click="login" class="btn btn-md btn-info">
                    <Icon icon="material-symbols:check-rounded" width="24" height="24" />
                    Iniciar Sesión
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
            error: null,
            formError: {}
        };
    },
    components: {
        TextInput,
        PasswordInput,
        Icon
    },
    methods: {
        ...mapActions(useStore, ['setToken']),
        async login() {
            try {
                let response = await this.$api.getUserToken(this.user)
                this.login(response.access)
                this.$emit('closeForm')
            } catch (err) {
                this.formError = err.response.data
            }
        }
    }
};
</script>