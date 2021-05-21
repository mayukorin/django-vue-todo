<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="8">
                <v-card>
                    <v-card-title>
                        <span class="headline">Username Update Page</span>
                    </v-card-title>
                    <v-card-text>
                        <v-form class="px-3" ref="form" v-model="valid">
                            <v-text-field 
                                label="ユーザ名"
                                v-model="form.username"
                                :rules="rules.username"
                                :counter="70"
                                maxlength="70"
                                prepend-icon="mdi-account"
                            >
                            </v-text-field>
                            <v-text-field 
                                label="パスワード"
                                v-model="form.check_password"
                                :rules="rules.password"
                                maxlength="20"
                                prepend-icon="mdi-lock"
                            >
                            </v-text-field>
                        </v-form>
                        <v-btn
                            class="success mx-0 mt-3"
                            @click="UsernameUpdate"
                        >更新</v-btn
                        >
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import api from "@/services/api";
export default {
    data:() => ({
        form: {
            username: '',
        },
        rules: {
            username: [
                v=> !!v || 'ユーザ名を入力してください',
            ],
            password: [
                v => !!v || 'password'
            ]
        },
        valid: true,
    }),
    created() {
        this.form.username = this.$store.state.auth.username;
    },
    methods: {
        UsernameUpdate: function() {
            if (this.$refs.form.validate()) {
                api({
                    method: "patch",
                    url: "user/profile/update/",
                    data: {
                        username: this.form.username,
                        confirm_password: this.form.check_password
                    }
                }).then(response => {
                    this.$store.dispatch("auth/logout");
                    this.$store.dispatch(
                        "auth/login", {
                            email: response.data.email,
                            password: this.form.check_password
                        }
                    ).then(() => {
                        console.log("Username Update succeeded.");
                        this.$store.dispatch("message/setInfoMessage", {
                            message: "Usernameを変更しました．"
                        });
                        this.$store.dispatch("message/setIsShowTrue");
                        console.log("kokomade")
                        console.log(this.$store.state.message.is_show);
                        this.$router.replace("/user-edit");
                    });

                });
            }
        }
    }

}
</script>