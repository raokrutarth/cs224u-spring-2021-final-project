# Results for final project

## Original untouched dataset with a 80/20 train/test split

### Grid search and results

```text
Experiment # 1
    directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
    early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
    l1_ratio=0.15, learning_rate='optimal', loss='hinge',
    max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
    power_t=0.5, random_state=None, shuffle=True, tol=0.001,
    validation_fraction=0.1, verbose=0, warm_start=False) 0.6029480166936947
Experiment # 2
    directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.2848686415176567
Experiment # 3
    simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
    early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
    l1_ratio=0.15, learning_rate='optimal', loss='hinge',
    max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
    power_t=0.5, random_state=None, shuffle=True, tol=0.001,
    validation_fraction=0.1, verbose=0, warm_start=False) 0.5662946370235287
Experiment # 4
    simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.25953857129232943

----BEST SYSTEM----
Best performing system score: 0.6029480166936947
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function directional_bag_of_words_featurizer_original_system at 0x7fd87eb2a200>,
              'factory_model': <function <lambda> at 0x7fd87fb0b0e0>}

relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.831      0.435      0.703        340       5716
author                    0.799      0.662      0.767        509       5885
capital                   0.395      0.316      0.376         95       5471
contains                  0.851      0.636      0.797       3904       9280
film_performance          0.822      0.689      0.792        766       6142
founders                  0.825      0.461      0.713        380       5756
genre                     0.695      0.335      0.572        170       5546
has_sibling               0.863      0.253      0.582        499       5875
has_spouse                0.894      0.340      0.674        594       5970
is_a                      0.753      0.282      0.564        497       5873
nationality               0.722      0.189      0.462        301       5677
parents                   0.821      0.574      0.756        312       5688
place_of_birth            0.609      0.240      0.466        233       5609
place_of_death            0.521      0.157      0.356        159       5535
profession                0.782      0.275      0.571        247       5623
worked_at                 0.789      0.310      0.603        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.748      0.385      0.610       9248      95264
```

Common relation combinations in training

```text
112 ('place_of_birth', 'place_of_death')
49 ('nationality', 'place_of_birth')
7 ('nationality', 'place_of_death')
5 ('adjoins', 'contains')
3 ('has_sibling', 'has_spouse')
2 ('parents', 'worked_at')
2 ('nationality', 'place_of_birth', 'place_of_death')
1 ('nationality', 'worked_at')
1 ('has_spouse', 'parents')
1 ('author', 'founders')
```

## With NELL relations added to the training set

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.5767462395301031
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.27757827786161005
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.5466324581330637
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.2618414354462869
----BEST SYSTEM----
Best performing system score: 0.5767462395301031
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function directional_bag_of_words_featurizer_original_system at 0x7f49c4cc1830>, 'factory_model': <function <lambda> at 0x7f49c80a1b90>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.732      0.497      0.669        340       5716
author                    0.761      0.694      0.746        509       5885
capital                   0.410      0.358      0.398         95       5471
contains                  0.663      0.908      0.701       3904       9280
film_performance          0.765      0.753      0.763        766       6142
founders                  0.741      0.482      0.669        380       5756
genre                     0.642      0.465      0.597        170       5546
has_sibling               0.781      0.265      0.562        499       5875
has_spouse                0.824      0.364      0.658        594       5970
is_a                      0.640      0.340      0.544        497       5873
nationality               0.528      0.286      0.451        301       5677
parents                   0.796      0.577      0.740        312       5688
place_of_birth            0.621      0.275      0.496        233       5609
place_of_death            0.471      0.208      0.376        159       5535
profession                0.601      0.372      0.536        247       5623
worked_at                 0.734      0.376      0.617        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.669      0.451      0.595       9248      95264
```

### Other relevant info

Count of relations added:

```text
Training KB before:  KB with 36,636 triples
Training KB after NELL relation addition:  KB with 46,772 triples
```

Examples of NELL relations

```text
KBTriple(rel='contains', sbj='Pennsylvania', obj='Arnold_Clavio'),
KBTriple(rel='has_spouse', sbj='Grace_Coolidge', obj='Winifred_Wagner'),
KBTriple(rel='contains', sbj='Massachusetts', obj='Majel_Barrett'),
KBTriple(rel='contains', sbj='Georgia', obj='Atlanta'),
KBTriple(rel='genre', sbj='Antonio_Banderas', obj='Rocky'),
KBTriple(rel='profession', sbj="Mrs._Warren's_Profession", obj='Architect'),
KBTriple(rel='contains', sbj='Illinois_Institute_of_Technology', obj='Pieria'),
KBTriple(rel='has_sibling', sbj='Black_Athena', obj='Lo!'),
KBTriple(rel='has_sibling', sbj='Dennis_Quaid', obj='John_Crome'),
KBTriple(rel='capital', sbj='Nova_Scotia', obj='Halifax_Regional_Municipality')
KBTriple(rel='contains', sbj='Nordic_countries', obj='Belize'),
KBTriple(rel='has_spouse', sbj='Ali', obj='Benjamin'),
KBTriple(rel='genre', sbj='Pope_Clement_VII', obj='Fly'),
KBTriple(rel='has_sibling', sbj='Fidel_Castro', obj='Charles_Perrault'),
KBTriple(rel='has_spouse', sbj='Carla_Gugino', obj="Paul_O'Grady"),
KBTriple(rel='contains', sbj='Nordic_countries', obj='Czech_Republic'),
KBTriple(rel='contains', sbj='Nordic_countries', obj='Germany'),
KBTriple(rel='contains', sbj='Nebraska', obj='Ali_Gomaa'),
KBTriple(rel='contains', sbj='Nordic_countries', obj='Gulf_of_Finland'),
KBTriple(rel='genre', sbj='Rocky', obj='The_Bean_Trees')
```

Common relation combinations in training:

```text
969 ('is_a', 'profession')
430 ('capital', 'contains')
112 ('place_of_birth', 'place_of_death')
49 ('nationality', 'place_of_birth')
9 ('has_sibling', 'has_spouse')
7 ('nationality', 'place_of_death')
7 ('has_spouse', 'parents')
7 ('contains', 'has_spouse')
7 ('adjoins', 'contains')
4 ('has_sibling', 'parents')
2 ('parents', 'worked_at')
2 ('nationality', 'place_of_birth', 'place_of_death')
2 ('has_spouse', 'profession')
2 ('contains', 'has_sibling', 'profession')
1 ('nationality', 'worked_at')
1 ('contains', 'genre')
1 ('author', 'founders')
1 ('adjoins', 'capital', 'contains')
1 ('adjoins', 'capital')
```

## With DocRED relations added to the training set

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.5396189549158068
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.26338510651556724
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.514440050756261
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.24062263585395263
----BEST SYSTEM----
Best performing system score: 0.5396189549158068
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function directional_bag_of_words_featurizer_original_system at 0x7f49dff56680>, 'factory_model': <function <lambda> at 0x7f49e39af440>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.749      0.482      0.674        340       5716
author                    0.510      0.811      0.551        509       5885
capital                   0.379      0.379      0.379         95       5471
contains                  0.625      0.909      0.667       3904       9280
film_performance          0.754      0.751      0.753        766       6142
founders                  0.772      0.489      0.692        380       5756
genre                     0.597      0.471      0.567        170       5546
has_sibling               0.693      0.339      0.573        499       5875
has_spouse                0.764      0.387      0.640        594       5970
is_a                      0.647      0.368      0.562        497       5873
nationality               0.506      0.259      0.425        301       5677
parents                   0.796      0.599      0.747        312       5688
place_of_birth            0.294      0.614      0.328        233       5609
place_of_death            0.194      0.560      0.223        159       5535
profession                0.626      0.352      0.542        247       5623
worked_at                 0.684      0.376      0.588        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.599      0.509      0.557       9248      95264
```

### Other relevant info

Count of relations added:

```text
Training KB before:  KB with 46,772 triples
Training KB after DocRED relation addition:  KB with 87,059 triples
```

Examples of DocRed relations

```text
KBTriple(rel='place_of_birth', sbj='E._Nesbit', obj='East_Baton_Rouge_Parish'),
KBTriple(rel='place_of_birth', sbj='De-Lovely', obj='Nico'),
KBTriple(rel='place_of_death', sbj='Elijah_Muhammad', obj='Gawker_Media'),
KBTriple(rel='has_sibling', sbj='Charales', obj='Pepin_the_Short'),
KBTriple(rel='has_spouse', sbj='Art', obj='Eve'),
KBTriple(rel='has_spouse', sbj='David', obj='Ife'),
KBTriple(rel='place_of_birth', sbj='Lae', obj='Stockholm'),
KBTriple(rel='place_of_birth', sbj='Samuel', obj='Northeast_Philadelphia'),
KBTriple(rel='place_of_birth', sbj='Yagan', obj='Western_Australia'),
KBTriple(rel='contains', sbj='County_Durham', obj='Art')
KBTriple(rel='place_of_death', sbj='Jean-Claude_La_Marre', obj='East_Baton_Rouge_Parish'),
KBTriple(rel='place_of_birth', sbj='Carmel-by-the-Sea', obj='Oman'),
KBTriple(rel='place_of_birth', sbj='Augustus', obj='Christchurch'),
KBTriple(rel='capital', sbj='Russia', obj='Moscow'),
KBTriple(rel='capital', sbj='Al-Saadi_Gaddafi', obj='Syria'),
KBTriple(rel='has_spouse', sbj='Edward_VII', obj='Alexandria'),
KBTriple(rel='place_of_death', sbj='Saint-Denis', obj='Rome'),
KBTriple(rel='place_of_death', sbj='Lucian', obj='Madrid'),
KBTriple(rel='author', sbj="Savai'i", obj='Jackie_Chan'),
KBTriple(rel='contains', sbj="People's_Songs", obj='Ngari_Prefecture')
```

Common relation combinations in training:

```text
2026 ('place_of_birth', 'place_of_death')
969 ('is_a', 'profession')
892 ('capital', 'contains')
72 ('has_sibling', 'has_spouse')
58 ('nationality', 'place_of_birth')
22 ('has_sibling', 'place_of_birth')
20 ('author', 'has_sibling')
18 ('capital', 'place_of_birth')
16 ('adjoins', 'contains')
15 ('capital', 'place_of_birth', 'place_of_death')
14 ('contains', 'place_of_birth')
14 ('author', 'place_of_birth')
13 ('has_spouse', 'place_of_death')
13 ('contains', 'has_spouse')
13 ('capital', 'place_of_death')
11 ('nationality', 'place_of_death')
10 ('has_spouse', 'place_of_birth')
10 ('author', 'has_spouse')
9 ('has_spouse', 'place_of_birth', 'place_of_death')
9 ('has_sibling', 'place_of_birth', 'place_of_death')
9 ('has_sibling', 'parents')
9 ('capital', 'contains', 'place_of_birth', 'place_of_death')
9 ('capital', 'contains', 'place_of_birth')
8 ('has_spouse', 'parents')
7 ('author', 'place_of_death')
7 ('author', 'contains')
7 ('author', 'capital')
```

## With only Declarative sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.32656686153150216
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.11450953575326622
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.33513898296817873
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.11405895956860271
----BEST SYSTEM----
Best performing system score: 0.33513898296817873
{'feauturizer': 'simple_bag_of_words_featurizer', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function simple_bag_of_words_featurizer at 0x7f498935b440>, 'factory_model': <function <lambda> at 0x7f498935b8c0>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.139      0.241      0.151        340       5716
author                    0.488      0.652      0.513        509       5885
capital                   0.125      0.368      0.144         95       5471
contains                  0.562      0.837      0.602       3904       9280
film_performance          0.394      0.706      0.432        766       6142
founders                  0.313      0.524      0.341        380       5756
genre                     0.174      0.324      0.192        170       5546
has_sibling               0.383      0.407      0.388        499       5875
has_spouse                0.329      0.672      0.367        594       5970
is_a                      0.398      0.431      0.404        497       5873
nationality               0.332      0.502      0.356        301       5677
parents                   0.461      0.641      0.488        312       5688
place_of_birth            0.258      0.395      0.277        233       5609
place_of_death            0.230      0.302      0.241        159       5535
profession                0.314      0.433      0.332        247       5623
worked_at                 0.201      0.417      0.224        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.319      0.491      0.341       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 13,369 examples
```

Examples of declarative sentences:

```text
'Scheme generates about 4,500GWh annually . The water travels through large hydro-electric power stations and generates clean , renewable , peak-load power . The power is distributed to the Australian Capital Territory , New South Wales , and Victoria . Water is also diverted to farms . Solar Solar energy sources are being harnessed on a small scale . Solar power contributes between',
 "and Gorin , respectively . [ 18 ] In the 1971 Peter Watkins film Punishment Park , members of the counter-culture are put on trial for similar `` crimes '' . Like Black Panther Party activist Bobby Seale , one of the African-American defendants is bound and gagged . Woody Allen satirized the trial in his 1971 film Bananas . Allen 's character , Fielding Melish ,", "a new sketch show named Horne and Corden , a `` traditional '' comedy show in the style of Morecambe and Wise [ 13 ] as well as the film Lesbian Vampire Killers . In February 2009 , he co-presented the Brit Awards with Mathew Horne and Kylie Minogue . On Friday 13 March 2009 , he appeared in a sketch for Comic Relief giving the England Football Team", "cousin , she of the driveway poster waving bye-bye to Darth and Shrub , sent me this in email . Obama 's our people ! `` He 's as Irish as bacon '' ! Moneygall is a small village in County Offaly , Ireland . It has a population of 298 people , has a Roman Catholic church , five shops , a post office , a national school , a police station"
```

## With only Imperative sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.45459077886921034
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.2008176107463705
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.4434174782667337
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.18156723581035863
----BEST SYSTEM----
Best performing system score: 0.45459077886921034
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function directional_bag_of_words_featurizer_original_system at 0x7f49dd18edd0>, 'factory_model': <function <lambda> at 0x7f493d5a2320>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.627      0.538      0.607        340       5716
author                    0.538      0.772      0.573        509       5885
capital                   0.336      0.442      0.353         95       5471
contains                  0.659      0.854      0.690       3904       9280
film_performance          0.571      0.675      0.589        766       6142
founders                  0.503      0.671      0.529        380       5756
genre                     0.256      0.359      0.272        170       5546
has_sibling               0.491      0.164      0.351        499       5875
has_spouse                0.393      0.731      0.433        594       5970
is_a                      0.475      0.527      0.485        497       5873
nationality               0.391      0.688      0.428        301       5677
parents                   0.469      0.708      0.503        312       5688
place_of_birth            0.350      0.489      0.371        233       5609
place_of_death            0.208      0.126      0.184        159       5535
profession                0.471      0.522      0.480        247       5623
worked_at                 0.475      0.434      0.466        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.451      0.544      0.457       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 91,546 examples
```

Examples of Imperative sentences:

```text
"10/02/2007 11:10:00 PM No comments : Labels : DAIO , Drawing I forgot this ! Work Cited Vincent van Gogh ( 1853-1890 ) , Cafe-Terrace At Night , Kröller-MÌller Museum in Otterlo , Netherlands . Posted by cindy at 10/02/2007 11:05:00 PM No comments : Labels : DAIO , Drawing Julie Park - `` Monet 's Painting '' Julie Park Monet Painting Monet is", "Ah - was on a canal between the Euphrates and Tigris rivers , it could never have been a Syrian city , but rather in present day Iraq , somewhere in the Baghdad area . Dr Fernie refers widely to Jewish studies , probably quoted from a former botanist Robert Turner . ^ `` Lavender '' . Oxford English Dictionary ( second ed. ) . 1989 Sources", 'the Vampire Slayer , Angel and Roswell , and has many times been noted for its mixing of multiple genres ( from horror and fantasy to comedy and even soap ) , as well as continuing after a number of archetypal jump the shark moments , most famously the departure of one of the leading actresses at', "three siblings , older brother , Liban , and Sagal left their homeland and joined relatives in New York City , where they stayed briefly before moving to Canada , to the Rexdale neighbourhood of Toronto , where there was a large Somali community and his family still resides . There , K'naan began learning English , partly by listening to", 'to raise awareness of and attract support for campaign finance reform . Granny D walked ten miles each day for 14 months , traversing California , Arizona , New Mexico , Texas , Arkansas , Tennessee , Kentucky , Ohio , West Virginia , Pennsylvania , Maryland , Virginia , and the District of Columbia , making'
```

## With only Interrogative sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.272800228873441
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12869627956425
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.2875422903281135
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12170614372425388
----BEST SYSTEM----
Best performing system score: 0.2875422903281135
{'feauturizer': 'simple_bag_of_words_featurizer', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function simple_bag_of_words_featurizer at 0x7f4981fd9200>, 'factory_model': <function <lambda> at 0x7f4981fd9b90>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.052      0.479      0.063        340       5716
author                    0.385      0.642      0.419        509       5885
capital                   0.118      0.305      0.134         95       5471
contains                  0.544      0.831      0.584       3904       9280
film_performance          0.385      0.657      0.419        766       6142
founders                  0.255      0.405      0.275        380       5756
genre                     0.157      0.400      0.179        170       5546
has_sibling               0.377      0.347      0.370        499       5875
has_spouse                0.285      0.625      0.320        594       5970
is_a                      0.335      0.414      0.348        497       5873
nationality               0.343      0.558      0.372        301       5677
parents                   0.293      0.516      0.320        312       5688
place_of_birth            0.239      0.391      0.260        233       5609
place_of_death            0.163      0.277      0.178        159       5535
profession                0.262      0.364      0.277        247       5623
worked_at                 0.148      0.240      0.160        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.271      0.466      0.292       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 2,756 examples
```

Examples of interrogative sentences:

```text
'Middle East along with a congressional delegation that included Evan Bayh , Kit Bond , and Harold Ford Jr . His trip included visits to Kuwait , Iraq , Israel , and the Palestinian territories . In Kuwait and Iraq , Obama visited with the troops . While in Iraq Obama stated , `` there is not', 'in and week out and this week vs Jacksonville who the Texans always play well against . Foster to have a big day as well as Schaub and Johnson . Jones-drew would be the only Jaguar worth starting this week . Tom Brady is a great start for big numbers at home vs Arizona . Don ’ t see Kevin', 'the voices of Tom Hanks and Tim Allen . It was written by John Lasseter , Andrew Stanton , Joel Cohen , Alec Sokolow , and Joss Whedon , and featured music by Randy Newman . Its executive producer was Steve Jobs with Edwin Catmull . Toy Story follows a group of anthropomorphic toys who pretend to be lifeless', 'created . Some pointed out that it would have been a foot too far for anyone to climb , which seems a tad oblivious to records like Illmatic , the Marshall Mathers LP and Doggystyle , all of which arrived tied to relatively similar expectations . As some observers pointed out , Drake is a very gifted rapper . When he', 'was introduced to music at an early age , singing in church with her mother . She admired stars such as Kay Starr , Jo Stafford , Hank Williams , Judy Garland , and Shirley Temple . She had perfect pitch . She was self-taught and could not read music . When she was thirteen , she was hospitalized'
```

## With only Exclamatory sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.5376881576267383
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.21924236308360545
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.501276900432727
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.19785428084839773
----BEST SYSTEM----
Best performing system score: 0.5376881576267383
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function directional_bag_of_words_featurizer_original_system at 0x7f49188f38c0>, 'factory_model': <function <lambda> at 0x7f4917c7e560>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.694      0.474      0.635        340       5716
author                    0.733      0.670      0.720        509       5885
capital                   0.400      0.316      0.380         95       5471
contains                  0.669      0.881      0.702       3904       9280
film_performance          0.619      0.731      0.639        766       6142
founders                  0.626      0.432      0.574        380       5756
genre                     0.663      0.371      0.573        170       5546
has_sibling               0.756      0.261      0.548        499       5875
has_spouse                0.686      0.423      0.610        594       5970
is_a                      0.614      0.292      0.503        497       5873
nationality               0.395      0.292      0.369        301       5677
parents                   0.784      0.535      0.717        312       5688
place_of_birth            0.560      0.202      0.413        233       5609
place_of_death            0.472      0.107      0.281        159       5535
profession                0.603      0.283      0.492        247       5623
worked_at                 0.647      0.318      0.536        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.620      0.412      0.543       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 159,088 examples
```

Examples of exclamatory sentences:

```text
"although she determined to succeed any task she dose n't think it through before doing most things , she is the guardian of courage her symbol is a star and her main color is red and her zoot is Zora . Haemi Haemi is sweet girl who try 's to see the best in life she unlike Chaney , thinks before she does", 'day a week together to try out some new flies that we might use in the upcoming two day contest that takes place on the Snake River in Wyoming and the South Fork in Idaho . We always get hooked on a couple new fun patterns but in the end , I usually fish a', 'climbs over 3,000ft high . Most rock climbers just call this climb “ El Cap. ” The top of El Capitan can be reached by hiking out of Yosemite Valley on the trail next to Yosemite Falls , then proceeding west . For climbers , the challenge is to climb up the sheer granite face ; there are many named climbing routes , all of', "during live shows . For instance , the set list usually includes renditions of `` Bang Bang ( My Baby Shot Me Down ) `` ( a song written by Sonny Bono and popularized by both Cher and Nancy Sinatra ) and `` Headin ' for the Texas Border '' by The Flamin ' Groovies . Other songs the band has covered include Gnarls Barkley 's", 'it interests us : What books or authors and/or illustrators influenced you as an early reader ? Chris : Richard Adams ( author ) , N.C.Wyeth , E.B . White , Ernest Shepard , Arnold Lobel . 4 . 7-Imp : If you could have three ( living ) illustrators—whom you have not yet met—over for coffee or a glass of rich , red wine ,'

```

## With only _ sentences in training corpus

### Grid search and results

```text
```

### Other relevant info

Count of corpus examples:

```text

```

Examples of exclamatory sentences:

```text

```

## With only Exclamatory sentences in training corpus

### Grid search and results

```text
```

### Other relevant info

Count of corpus examples:

```text

```

Examples of exclamatory sentences:

```text

```

## With only Exclamatory sentences in training corpus

### Grid search and results

```text
```

### Other relevant info

Count of corpus examples:

```text

```

Examples of exclamatory sentences:

```text

```

## With only Exclamatory sentences in training corpus

### Grid search and results

```text
```

### Other relevant info

Count of corpus examples:

```text

```

Examples of exclamatory sentences:

```text

```

## With only Exclamatory sentences in training corpus

### Grid search and results

```text
```

### Other relevant info

Count of corpus examples:

```text

```

Examples of exclamatory sentences:

```text

```

## Unknown expriment during model development

```text
#SGD_factory, default loss function: 0.611
#SGD_factory, log loss function: 0.581
#SGD_factory, modified_huber loss function: 0.588
#SGD_factory, squared_hinge loss function: 0.456
#SGD_factory, perceptron loss function: 0.502
#SGD_factory, squared_loss loss function: 0.109
#SGD_factory, huber loss function: 0.397
#SGD_factory, epsilon_insensitive loss function: 0.5
#SGD_factory, squared_epsilon_insensitive loss function: 0.089
"""
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.796      0.424      0.677        340       5716
author                    0.845      0.654      0.799        509       5885
capital                   0.545      0.189      0.396         95       5471
contains                  0.847      0.627      0.792       3904       9280
film_performance          0.864      0.658      0.813        766       6142
founders                  0.819      0.476      0.716        380       5756
genre                     0.635      0.318      0.529        170       5546
has_sibling               0.783      0.275      0.571        499       5875
has_spouse                0.873      0.335      0.661        594       5970
is_a                      0.731      0.296      0.565        497       5873
nationality               0.765      0.249      0.541        301       5677
parents                   0.871      0.564      0.786        312       5688
place_of_birth            0.778      0.210      0.505        233       5609
place_of_death            0.655      0.119      0.345        159       5535
profession                0.733      0.300      0.568        247       5623
worked_at                 0.672      0.322      0.552        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.763      0.376      0.614       9248      95264
Experiment # 1 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.612025870865468
Experiment # 2 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.2780895197041119
Experiment # 3
    simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
    early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
    l1_ratio=0.15, learning_rate='optimal', loss='hinge',
    max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
    power_t=0.5, random_state=None, shuffle=True, tol=0.001,
    validation_fraction=0.1, verbose=0, warm_start=False)
    0.5520678361770706

Experiment # 4
    simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.26078986141577176
----BEST SYSTEM----
Best performing system score: 0.612025870865468
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False)}
"""
```
