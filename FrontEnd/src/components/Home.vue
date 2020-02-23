<template>
    <div id="body">
        <div id="title">
            <h1>{{ home }}</h1>
        </div>
    </div>
</template>

<script>export default {
        name: 'Home',
        props: {
            home: String,
            stats: String
        }
    }</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #title {
        left: 100px
    }

    il {
        font-size: 10px
    }

    h1 {
        left: 100px;
        color: #345235;
    }
</style>