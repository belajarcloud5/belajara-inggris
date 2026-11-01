from qk import mk, mkf, mko
PASS = dict(practice=mk([
 ('Pilih jawaban yang benar: "The data ___ collected in May."', "was", "were to", "is", "has", "Lampau tunggal → was collected."),
 ('Pilih jawaban yang benar: "The survey ___ completed by staff."', "was", "were", "is been", "has", "Tunggal lampau → was."),
 ('Pilih jawaban yang benar: "The figures will ___ reviewed."', "be", "is", "been", "being", "will be + V3."),
 ('Pilih jawaban yang benar: "The results ___ analyzed last week."', "were", "was", "is", "has", "Jamak lampau → were."),
 ('Pilih pasif dari "We collected the data.":', "The data was collected.", "The data collected.", "The data is collecting.", "The data were collecting.", "was + V3."),
 ('Pilih pasif dari "We will review the figures.":', "The figures will be reviewed.", "The figures will review.", "The figures will been reviewed.", "The figures will reviewed.", "will be + V3."),
 ('Pilih kalimat yang SALAH:', "The report was submit on Friday.", "The report was submitted on Friday.", "The reports were submitted on Friday.", "The report will be submitted.", "V3: submitted."),
]) + mkf([
 ("Datanya dikumpulkan pada bulan Mei.", "The data was ___ in May.", "collected", "was + V3."),
 ("Survei diselesaikan oleh staf.", "The survey was ___ by staff.", "completed", "was + V3."),
 ("Angkanya akan ditinjau.", "The figures will be ___.", "reviewed", "will be + V3."),
 ("Hasilnya dianalisis.", "The results were ___.", "analyzed", "were + V3."),
]), quiz=mk([
 ('Pilih jawaban yang benar: "The sales ___ recorded daily."', "are", "is", "does", "has", "Jamak → are recorded."),
 ('Pilih jawaban yang benar: "The report ___ been approved."', "has", "have", "is", "was", "has been + V3."),
 ('Pilih kalimat yang SALAH:', "The figures was reviewed.", "The figures were reviewed.", "The figure was reviewed.", "The figures will be reviewed.", "figures jamak → were."),
]) + mkf([
 ("Laporan sudah diserahkan.", "The report has been ___.", "submitted", "has been + V3."),
]))
