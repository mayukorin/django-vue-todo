<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="8">
                <v-card>
                    <v-card-title>
                        <span class="headline">Email Update Page</span>
                    </v-card-title>
                    <v-card-text>
                        <v-form class="px-3" ref="form" v-model="valid">
                            <v-text-field 
                                label="メールアドレス"
                                v-model="form.email"
                                :rules="EmailRule"
                                :counter="70"
                                maxlength="70"
                                prepend-icon="mdi-email"
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
                            @click="EmailUpdate"
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
            email: '',
            check_password: '',
        },
        rules: {
            email: [
                v => !!v || 'メールアドレスを入力してください',
                v => /.+@.+/.test(v) || 'メールアドレスの形式が間違っています',
            ],
            password: [
                v => !!v || 'パスワードを入力してください',
            ]
        },
        valid: true,
    }),
    created() {
        this.form.email = this.$store.state.auth.email;
    },
    computed: {
        EmailRule() {
            const rules = []
            if (this.form.email == '') rules.push('メールアドレスを入力してください')
            else if (/.+@.+/.test(this.form.email) == false) rules.push('メールアドレスの形式が間違っています')
            else if (this.form.email == this.$store.state.auth.email) rules.push('現在とは異なるメールアドレスを入力してください')
            return rules
        }
    },
    methods: {
        nowEmailMatchRule :function(value) {
            if (value == this.$store.state.auth.email) return '現在とは異なるメールアドレスを入力してください';
            else return true;
        },
        EmailUpdate: function() {
            if (this.$refs.form.validate()) {
                api({
                    method: "patch",
                    url: "user/profile/update/",
                    data: {
                        email: this.form.email,
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
                        console.log("Email Update succeeded.");
                        this.$store.dispatch("message/setInfoMessage", {
                            message: "メールアドレスを変更しました．"
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