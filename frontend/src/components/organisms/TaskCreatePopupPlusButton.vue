<template>
    <v-dialog max-width="600px" v-model="dialog">
        <template v-slot:activator="{ on: popup, attrs }">
            <v-tooltip top>
                <template v-slot:activator="{ on: tooltip }" >
                    <v-btn
                        class="ma-2"
                        fab
                        dark
                        text
                        color="success"
                        v-bind="attrs"
                        v-on="{ ...tooltip, ...popup }"
                    >
                        <v-icon dark>
                            mdi-plus
                        </v-icon>
                    </v-btn>
                </template>
                <span>タスク新規作成</span>
            </v-tooltip>
        </template>
        <TaskCreateCard @dialog-false="dialogFalse" />
    </v-dialog>
</template>
<script>
import TaskCreateCard from '@/components/organisms/TaskCreateCard';
export default {
    name: 'TaskCreatePopupPlusButton',
    components: {
        TaskCreateCard,
    },
    data: () => ({
        dialog: false,
    }),
    methods: {
        dialogFalse() {
            this.dialog = false;
        }
    },
};
</script>