import 'survey-core/defaultV2.min.css';
import { Model } from 'survey-core';
import { Survey } from 'survey-react-ui';
import "survey-core/defaultV2.min.css";
import { json } from "./json";

const surveyJson = {
    elements: [{
        name: "Município",
        title: "Preencha o Município:",
        type: "text"
    }, {
        name: "LastName",
        title: "Enter your last name:",
        type: "text"
    }]
};

function SurveyComponent() {
    const survey = new Model(json);
    survey.onComplete.add((sender, options) => {
        console.log(JSON.stringify(sender.data, null, 3));
    });
    return (<Survey model={survey} />);
}



function App() {
    const survey = new Model(surveyJson);

    return SurveyComponent();
}

export default App;
