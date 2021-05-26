<template>
    <v-navigation-drawer app v-model="drawer" class="primary">
        <v-row v-if="true">
            <v-col class="text-center mt-4 mb-3">
                <TaskCreatePopup />
            </v-col>
        </v-row>
        <v-list>
            <v-list-item router to="/user-edit">
                <v-list-item-icon>
                    <v-icon class="white--text">mdi-account</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title class="white--text">Account Edit</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
        <v-list>
            <v-list-item router to="/user-create">
                <v-list-item-icon>
                    <v-icon class="white--text">mdi-account</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title class="white--text">Account Create</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>
<script>
import TaskCreatePopup from "@/components/organisms/TaskCreatePopup";

export default {
    name: 'Drawer',
    components: {
        TaskCreatePopup
    },
    props: {
        drawerNotification: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            drawer: false
        }
    },
    watch: {
        drawerNotification() {
            this.drawer = !this.drawer;
        }
    }
};
</script>