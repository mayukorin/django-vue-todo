<template>
    <nav>
        <SnackBar />
        <Appbar @handleDrawer="drawerChange" />
        <Drawer :drawer-notification="drawerNotify" @handleDrawer="drawerChange" />
    </nav>
</template>
<script>
import SnackBar from './SnackBar';
import Appbar from './Appbar';
import Drawer from './Drawer';
export default {
    name: 'Navbar',
    components: { 
        Appbar,
        Drawer,
        SnackBar
    },
    data() {
        return {
            drawerNotify: false,
        }
    },
    methods: {
        drawerChange() {
            this.drawerNotify = !this.drawerNotify;
        }
    },
};
</script>
