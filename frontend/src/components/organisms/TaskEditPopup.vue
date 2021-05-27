<template>
    <div>
        <!-- @click.stopにいれればいける -->
        <div @click.stop="dialogTrue">
                <div class="caption grey--text">edit</div>
                <v-icon>mdi-pencil</v-icon>
        </div>
        <v-dialog v-model="dialog" max-width="600px">
            <TaskEditCard :task="task" @dialog-false="dialogFalse"/>
        </v-dialog>
    </div>
</template>
<script>
import api from "@/services/api";
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
    data: () => ({
        dialog: false,
    }),
    methods: {
        taskUpdate: function() {
            api({
                method: "patch",
                url: "/task/update/" + this.form.pk + "/",
                data: {
                    title: this.form.title,
                    content: this.form.content,
                    deadline: this.form.deadline
                }
            }).then(response => {
                console.log(response.data);
                this.$store.dispatch("tasks/setUpdateFlagTrue");//taskを更新するように
                this.$store.dispatch("message/setKeepInfoMessage", {
                    message: "タスクを更新しました"
                });
                this.dialog = false;
            })
        },
        dialogTrue() {
            this.dialog = true;
        },
        dialogFalse() {
            this.dialog = false;
        }
    },
};
</script>
