<template>
    <v-card>
        <v-card-title>
            <span class="headline">ユーザ名の変更</span>
        </v-card-title>
        <v-card-text>
            <UserNameUpdateForm :username="getUserNameInfo" :on-update="handleUpdate" />
            <div class="my-3">
                <router-link to="/user-profile">ユーザ情報一覧へ戻る</router-link>
            </div>
        </v-card-text>
    </v-card>
</template>
<script>
import UserNameUpdateForm from '@/components/molecules/UserNameUpdateForm';
export default {
    name: 'UserNameUpdateCard',
    components: {
        UserNameUpdateForm
    },
    methods: {
        handleUpdate(userInfo) {
            return this.$store.dispatch('auth/userNameUpdate', userInfo)
                .then(() => {
                    this.$store.dispatch('message/setInfoMessage', {
                        message: 'ユーザ名を変更しました．'
                    });
                    this.$router.replace('/user-profile');
                });
        }
    },
    computed: {
        getUserNameInfo() {
            return this.$store.state.auth.username
        }
    }

}
</script>