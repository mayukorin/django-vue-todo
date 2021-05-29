<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="8">
                <v-card>
                    <v-card-title>
                        <span class="headline">User Edit Page</span>
                    </v-card-title>
                    <v-card-text>
                        <v-list>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-subtitle>email</v-list-item-subtitle>
                                    <v-list-item-title>{{ preUser.email }}</v-list-item-title>
                                </v-list-item-content>
                                <v-list-item-action>
                                    <Button @click="GoUpdatePage('/email-update')">編集</Button>
                                </v-list-item-action>
                            </v-list-item>
                            <v-divider></v-divider>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-subtitle>username</v-list-item-subtitle>
                                    <v-list-item-title>{{ preUser.username }}</v-list-item-title>
                                </v-list-item-content>
                                <v-list-item-action>
                                    <Button @click="GoUpdatePage('/username-update')">編集</Button>
                                </v-list-item-action>
                            </v-list-item>
                            <v-divider></v-divider>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-subtitle>password</v-list-item-subtitle>
                                </v-list-item-content>
                                <v-list-item-action>
                                    <Button @click="GoUpdatePage('/password-update')">編集</Button>
                                </v-list-item-action>
                            </v-list-item>
                        </v-list>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import Button from '@/components/atoms/Button';
export default {
    components: {
        Button
    },
    data() {
        return {
            preUser: {
                email: '',
                username: ''
            }
        }
    },
    created() {
        this.preUser.email = this.$store.state.auth.email;
        this.preUser.username = this.$store.state.auth.username;
        console.log(this.$store.state.message);
    },
    methods: {
        GoUpdatePage: function(next_url) {
            this.$router.replace(next_url);
        }
    }
}
</script>
