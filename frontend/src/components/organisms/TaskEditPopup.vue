<template>
    <div>
        <div @click.stop="dialogTrue">
                <div class="caption grey--text">編集</div>
                <v-icon>mdi-pencil</v-icon>
        </div>
        <v-dialog v-model="dialog" max-width="600px">
            <TaskEditCard :task="task" @dialogFalse="dialogFalse"/>
        </v-dialog>
    </div>
</template>
<script>
import TaskEditCard from "@/components/organisms/TaskEditCard";

export default {
    name: 'TaskEdit',
    props: {
        task: {
            type: Object,
            required: true
        },
    },
    components: {
        TaskEditCard
    },
    data () {
        return {
            dialog: false,
        }
    },
    methods: {
        dialogTrue() {
            this.dialog = true;
        },
        dialogFalse() {
            this.dialog = false;
        }
    },
};
</script>
