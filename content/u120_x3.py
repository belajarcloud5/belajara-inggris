from ub import *
from ielts_h import ask
E1 = "To: Customer Service Team. From: Daniel Cruz, Operations Manager. Subject: New complaint procedure. Starting on June 1, all complaints must be recorded in the online system within one hour. Staff should not promise refunds without approval from a supervisor. Weekly meetings will be held every Monday at nine to review difficult cases. Please confirm that you have read this message."
N1 = "SUNRISE LANGUAGE CENTRE. New English courses start on September 5. Beginner and intermediate classes are held in the evenings, from six to eight, on Monday and Wednesday. The course fee is one hundred and twenty dollars, and students who register before August 20 receive a ten percent discount. Classes are limited to fifteen students. To register, visit our office on Park Street or fill in the form on our website."
P = ask(E1, [
 ("What is the purpose of the email?", "To explain a new procedure", "To announce a holiday", "To request a refund", "To invite staff to a party", "Subjek: New complaint procedure."),
 ("Within what time must complaints be recorded?", "One hour", "One day", "One week", "Ten minutes", "Within one hour."),
 ("What should staff NOT do?", "Promise refunds without approval", "Attend Monday meetings", "Record complaints online", "Confirm they read the message", "Tidak boleh janji refund."),
 ("When are the weekly meetings?", "Every Monday at nine", "Every Friday at nine", "On June 1", "Every day", "Monday at nine."),
 ("What are staff asked to do at the end?", "Confirm they have read the message", "Call the manager", "Send a report", "Attend training", "Please confirm."),
]) + ask(N1, [
 ("What is the notice mainly about?", "New English courses", "A new office", "A job opening", "A language test", "Gagasan utama."),
 ("When are the classes held?", "Evenings on Monday and Wednesday", "Mornings on weekends", "Afternoons every day", "Evenings on Friday", "Senin dan Rabu malam."),
 ("How can students get a discount?", "Register before August 20", "Bring a friend", "Pay in cash", "Join two courses", "Daftar sebelum 20 Agustus."),
 ("How many students are in a class?", "Up to fifteen", "Up to five", "Up to fifty", "Up to twenty-five", "Maksimal lima belas."),
 ("What is the course fee?", "One hundred and twenty dollars", "Twelve dollars", "One hundred dollars", "Two hundred dollars", "120 dolar."),
])
X3 = dict(practice=P[:8], quiz=P[8:])
