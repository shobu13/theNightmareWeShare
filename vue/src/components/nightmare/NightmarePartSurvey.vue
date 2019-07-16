<template>
    <div id="survey">
        <!-- Font Awesome -->
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
        <!-- Bootstrap core CSS -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css"
              rel="stylesheet">
        <!-- Material Design Bootstrap -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.5/css/mdb.min.css" rel="stylesheet">
        

        <div id="survey_ended" v-if="this.ended">
            <div class="card-text">temps restant : terminé</div>
            <table class="table table-hover table-striped">
                <thead>
                <tr>
                    <th scope="col">Choix</th>
                    <th scope="col">Votes</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="choice in this.survey.nightmaresurveypropositions" :key="choice.id">
                    <td>{{ choice.name }}</td>
                    <td>{{ choice.votes.length }}</td>
                </tr>

                </tbody>
            </table>
        </div>
        <div id="survey_progress" v-if="!this.ended">
            <div class="card-text" v-if="end">temps restant : {{ end.getMinutes() }} mn {{ end.getSeconds() }} s</div>
            <form class="text-left">
                <div class="form-check">
                    <div class="custom-control custom-radio" v-for="choice in this.survey.nightmaresurveypropositions"
                         :key="choice.id">
                        <input type="radio" class="custom-control-input"
                               :id="choice.name"
                               :value="choice.id" v-model="choice_picked">
                        <label class="custom-control-label"
                               :for="choice.name">{{ choice.name }}</label>
                    </div>
                    {{choice_picked}}
                </div>
                <input type="submit" class="btn btn-primary" value="Envoyer"/>
            </form>
        </div>
    </div>
</template>

<script>
    export default {

        props: ['id', 'end_date'],
        data: () => {
            return {
                end: undefined,
                ended: false,
                survey: {},
                choice_picked: undefined,
            }
        },
        mounted() {
            this.get_survey(this.id);
            this.update_time();
            this.interval = setInterval(() => {
                this.update_time();
            }, 1000);
        },
        methods: {
            update_time() {
                const date = new Date(this.end_date) - Date.now();
                this.end = new Date(date);
                if (date <= 0 && !this.ended) {
                    this.ended = true;
                }
            },
            get_survey() {
                axios.get(`http://127.0.0.1:8000/api/nightmareSurvey/${this.id}/`).then((data) => {
                    this.survey = data.data;
                })
            }
        }
    }
</script>

<style>

</style>
