from ielts_h import tfn
E1 = "Coral reefs cover less than one percent of the ocean floor, yet they support about a quarter of all marine species. Rising sea temperatures cause corals to lose their colour, a process called bleaching. Scientists have found that some reefs recover if the water cools within a few weeks. Tourism can also harm reefs when visitors touch or step on the coral."
E2 = "The town of Hallby introduced a ban on plastic bags in 2018. Shops now charge for paper bags, and most customers bring their own. A survey last year found that plastic waste on the town's beach had fallen by half. Some small shop owners complained that the new rules were confusing, but the council says it has no plans to change them."
I4 = dict(practice=tfn(E1, [
 ("Coral reefs cover more than ten percent of the ocean floor.", 'F', "Teks: less than one percent."),
 ("About a quarter of marine species live on reefs.", 'T', "Teks: about a quarter."),
 ("Bleaching is caused by rising sea temperatures.", 'T', "Teks menyebutnya."),
 ("All bleached reefs die.", 'F', "Teks: some reefs recover."),
 ("Tourism can damage reefs.", 'T', "Teks: can also harm reefs."),
 ("Reefs in the Pacific are healthier than those in the Atlantic.", 'N', "Tidak dibandingkan.")]) + tfn(E2, [
 ("Hallby banned plastic bags in 2018.", 'T', "Teks menyebutnya."),
 ("Shops give paper bags for free.", 'F', "Teks: shops now charge."),
 ("Plastic waste on the beach has halved.", 'T', "Fallen by half."),
 ("All shop owners support the new rules.", 'F', "Some complained."),
 ("The council plans to change the rules soon.", 'F', "Teks: no plans to change."),
 ("Most customers in Hallby are tourists.", 'N', "Tidak disebut.")]),
 quiz=tfn(E1, [
 ("Corals lose their colour in a process called bleaching.", 'T', "Disebut langsung."),
 ("Reefs recover only if the water stays warm.", 'F', "Teks: recover if the water cools."),
 ("Scientists have invented a way to rebuild reefs.", 'N', "Tidak disebut.")]) + tfn(E2, [
 ("The survey was carried out last year.", 'T', "Teks: a survey last year."),
 ("The ban applies to paper bags too.", 'F', "Paper bags masih dijual."),
 ("The rules are easy for everyone to understand.", 'F', "Some found them confusing.")]))
