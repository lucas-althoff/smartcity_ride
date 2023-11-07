import  { form } from "./main_form";
import { est_form } from "./estrategia";
import { inf_form } from "./infraestrutura";
import { dad_form } from "./dados";
import { serv_form } from "./servicos";
import { mon_form } from "./monitoramento";

export const finalForm = form;

finalForm["pages"].push(est_form);
finalForm["pages"].push(inf_form);
finalForm["pages"].push(dad_form);
finalForm["pages"].push(serv_form);
finalForm["pages"].push(mon_form);