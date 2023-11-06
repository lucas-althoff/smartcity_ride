import  { form } from "./main_form";
import { est_form } from "./estrategia";
import { inf_form } from "./infraestrutura";

export const finalForm = form;

finalForm["pages"].push(est_form);
finalForm["pages"].push(inf_form);