<template>
    <div id="user-create-page">
        <v-container class="my-5">
            <v-row justify="center">
                <v-col cols="8">
                    <v-card  class="user-create-card">
                        <v-card-title>
                            <span class="headline">User Create</span>
                        </v-card-title>
                        <v-card-text>
                            <v-form ref="form" v-model="valid">
                                    <v-text-field
                                        v-model="form.email"
                                        :counter="70"
                                        label="メールアドレス"
                                        :rules="rules.email"
                                        maxlength="70"
                                        prepend-icon="mdi-email"
                                    />
                                    <v-text-field
                                        v-model="form.username"
                                        :counter="70"
                                        label="ユーザ名"
                                        :rules="rules.username"
                                        maxlength="70"
                                        prepend-icon="mdi-account"
                                    />
                                    <v-text-field
                                        type="password"
                                        v-model="form.password"
                                        :counter="20"
                                        label="パスワード"
                                        :rules="rules.password"
                                        maxlength="20"
                                        prepend-icon="mdi-lock"
                                    />
                                <v-btn 
                                    class="success mx-0 mt-3" 
                                    @click="userCreate"
                                >登録</v-btn>
                            </v-form>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>
<script>
import api from "@/services/api";
export default {
    name: 'UserCreate',
    
    data: () => ({
        form: {
            email: '',
            username: '',
            password: '',
        },
        valid:true,
        loading:false,
        rules: {
            email: [
                v => !!v || 'メールアドレスを入力してください',
                v => /.+@.+/.test(v) || 'メールアドレスの形式が間違っています',
            ],
            username: [
                v => !!v || 'ユーザ名を入力してください',
            ],
            password: [
                v => !!v || 'パスワードを入力してください',
            ]

        }
    }),
    methods: {
        userCreate() {
            if (this.$refs.form.validate()) {
                api({
                    method: "post",
                    url: "/user/create/",
                    data: {
                        email: this.form.email,
                        username: this.form.username,
                        password: this.form.password
                    }
                }).then(response => {
                    console.log(response.data);
                    this.$store.dispatch("message/setInfoMessage", {
                        message: "ユーザ登録が完了しました．"
                        });
                    this.$router.replace("/login");//ログイン画面へ
                })
            }
        }
    }
};
</script>

