<template>
  <div id="login-page">
    <!--
    <v-container class="grid-list-md" style="height: 900px;">
      <v-layout row warp align-center justify-center fill-height>
        <v-flex xs12 sm8 lg4 md5>
          -->
          <v-container class="my-5">
            <v-row justify="center">
              <v-col cols="8">
                <v-card  class="login-card">
                  <v-card-title>
                    <span class="headline">Login to App</span>
                  </v-card-title>
                  <v-card-text>
                    <!--
                    <v-layout
                      row
                      fill-height
                      justify-center
                      align-center
                      v-if="loading"
                    >
                      <v-progress-circular :size="50" color="primary" indeterminate />
                    </v-layout>
                    -->
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
                          type="password"
                          v-model="form.password"
                          :counter="20"
                          label="パスワード"
                          :rules="rules.password"
                          maxlength="20"
                          prepend-icon="mdi-lock"
                        />
                        <v-spacer></v-spacer>
                      <v-btn
                        class="success mx-0 mt-3"
                        @click="login"
                        >Login</v-btn
                      >
                    </v-form>
                  </v-card-text>
                </v-card>
                <br />
                <router-link to="/user-create">ユーザ新規作成</router-link>
              </v-col>
            </v-row>
          </v-container>
          <!--
        </v-flex>
      </v-layout>
    </v-container>
    -->
  </div>
</template>

<script>
export default {
  
  data:() => ({
    form: {
      email: '',
      password: '',
    },
    valid: true,
    //loading: false,
    rules: {
      email: [
        v => !!v || 'メールアドレスを入力してください',
        v => /.+@.+/.test(v) || 'メールアドレスの形式が間違っています',
      ],
      password: [
        v=> !!v || 'パスワードを入力してください',
      ]
    }
  }),
  methods: {
        login() {
          if (this.$refs.form.validate()) {
            this.$store
                .dispatch("auth/login", {
                    email: this.form.email,
                    password: this.form.password
                })
                .then(() => {
                    console.log("Login succeeded.");
                    this.$store.dispatch("message/setKeepInfoMessage", {
                      message: "ログインしました．"
                    });
                    const next = this.$route.query.next || "/";
                    this.$router.replace(next);
                });
          }
        }
    }
};
</script>

