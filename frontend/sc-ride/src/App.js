import 'survey-core/defaultV2.min.css';
import { Model, FunctionFactory } from 'survey-core';
import { Survey } from 'survey-react-ui';
import "survey-core/defaultV2.min.css";
import {finalForm} from "./form/builder";
import { useCallback } from 'react';
// import { json } from "./json";

function validateLength(params) {
    const valArray = params[0];
    if (valArray.isNull) {
        return 0;
    }
    return valArray.length;
}


FunctionFactory.Instance.register("validateLength", validateLength);



function SurveyComponent() {
    const survey = new Model(finalForm);
    survey.onComplete.add((sender, options) => {
        console.log(JSON.stringify(sender.data, null, 3));
    });

    return (<Survey model={survey} />);
}



function App() {
    return SurveyComponent();
}

export default App;
