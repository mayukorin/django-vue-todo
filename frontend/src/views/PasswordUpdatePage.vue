<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="8">
                <v-card>
                    <v-card-title>
                        <span class="headline">Password Update Page</span>
                    </v-card-title>
                    <v-card-text>
                        <v-form class="px-3" ref="form" v-model="valid">
                            <v-text-field 
                                label="現在のpassword"
                                v-model="form.check_password"
                                :rules="rules.password"
                                maxlength="20"
                                prepend-icon="mdi-lock"
                            >
                            </v-text-field>
                            <v-text-field 
                                label="新しいpassword"
                                v-model="form.new_password"
                                :rules="rules.password"
                                maxlength="20"
                                prepend-icon="mdi-lock"
                            >
                            </v-text-field>
                            <v-btn
                                class="success mx-0 mt-3"
                                @click="update"
                            >更新</v-btn
                            >
                        </v-form>
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
            check_password: '',
            new_password: ''
        },
        rules: {
            password: [
                v=> !!v || 'パスワードを入力してください',
            ]
        },
        valid: true,
    }),
    methods: {
        update: function() {
            if (this.$refs.form.validate()) {
                console.log(this.form.check_password);
                console.log(this.form.new_password);
                api({
                    method: "patch",
                    url: "/password/update/",
                    data: {
                        confirm_password: this.form.check_password,
                        password: this.form.new_password
                    }
                }).then(response => {
                    //console.log(response.data);
                    this.$store.dispatch("auth/logout");
                    this.$store.dispatch(
                        "auth/login", {
                            email: response.data.email,
                            password: this.form.new_password
                        }
                    ).then(() => {
                        console.log("Password Update succeeded.");
                        this.$store.dispatch("message/setInfoMessage", {
                            message: "パスワードを変更しました．"
                        });
                        this.$store.dispatch("message/setIsShowTrue");
                        console.log("kokomade")
                        console.log(this.$store.state.message.is_show);
                        this.$router.replace("/user-edit");
                    });
                })
            }
        }
    }
}
</script>
