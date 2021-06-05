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

## With only History sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.4288254448517488
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.15389732579947102
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.39103807984606204
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.1408594704071694
----BEST SYSTEM----
Best performing system score: 0.4288254448517488
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function directional_bag_of_words_featurizer_original_system at 0x7f576ae47c20>, 'factory_model': <function <lambda> at 0x7f5769c9df80>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.479      0.500      0.483        340       5716
author                    0.551      0.782      0.586        509       5885
capital                   0.384      0.295      0.362         95       5471
contains                  0.658      0.843      0.688       3904       9280
film_performance          0.567      0.710      0.591        766       6142
founders                  0.412      0.611      0.441        380       5756
genre                     0.256      0.388      0.275        170       5546
has_sibling               0.354      0.525      0.378        499       5875
has_spouse                0.342      0.702      0.381        594       5970
is_a                      0.440      0.475      0.447        497       5873
nationality               0.378      0.631      0.411        301       5677
parents                   0.504      0.647      0.527        312       5688
place_of_birth            0.345      0.511      0.369        233       5609
place_of_death            0.248      0.421      0.270        159       5535
profession                0.348      0.462      0.366        247       5623
worked_at                 0.289      0.450      0.311        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.410      0.560      0.430       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 47,092 examples
```

Examples of sentences:

```text
"any song contains louder bass Jumpstyle is a rave dance and electronic music genre mainly practiced in Europe , specifically the Netherlands , Belgium , Germany and northern France . The dance is also called Jumpen ( English word Jump + the Dutch and German suffix -en , meaning `` to jump '' or `` jumping '' ) . Jumpstyle also refers", "the 1980s and 1990s . In addition to mainstream pop , many Bacharach songs were adapted by jazz artists of the time , such as Stan Getz , Cal Tjader and Wes Montgomery . The Bacharach/David composition , `` My Little Red Book '' , originally recorded by Manfred Mann for the film What 's New , Pussycat ? , and promptly covered by Love", 'for people who suffer from gluten intolerance , since rice does not contain gluten . Rye flour is used to bake the traditional sourdough breads of Germany , Austria , Switzerland , Russia , Czech Republic , Poland and Scandinavia . Most rye breads use a mix of rye and wheat flours because rye', '. [ 19 ] [ 20 ] He was a member of The Literary Society . He was a non-executive independent director of Times Newspaper holdings , the publishers of The Times and The Sunday Times from 1982 . [ 21 ] Private life John Gross was married to Miriam Gross , also a prominent literary editor , from 1965 to 1988 . The couple had', 'belief ( on the street , anyway ) , this is not the breed of dog from the movie Beethoven . It is not the breed of dog from Turner and Hooch . It is , however , the breed of dog from The Sandlot . We are hopelessly devoted . View the entire comment thread . Search Follow this blog Creative Partners Recent Posts Pretty Flowers All In a Row ... Tutorial and'
```

## With only Economics sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.20464742946053666
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12468643678932437
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.217286569898007
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12539387743410224
----BEST SYSTEM----
Best performing system score: 0.217286569898007
{'feauturizer': 'simple_bag_of_words_featurizer', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function simple_bag_of_words_featurizer at 0x7f5783d50680>, 'factory_model': <function <lambda> at 0x7f5782a3e050>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.044      0.447      0.054        340       5716
author                    0.305      0.737      0.346        509       5885
capital                   0.065      0.305      0.077         95       5471
contains                  0.490      0.793      0.530       3904       9280
film_performance          0.243      0.243      0.243        766       6142
founders                  0.224      0.624      0.257        380       5756
genre                     0.130      0.312      0.147        170       5546
has_sibling               0.292      0.297      0.293        499       5875
has_spouse                0.265      0.343      0.278        594       5970
is_a                      0.222      0.398      0.244        497       5873
nationality               0.190      0.585      0.220        301       5677
parents                   0.198      0.577      0.228        312       5688
place_of_birth            0.209      0.253      0.217        233       5609
place_of_death            0.124      0.289      0.140        159       5535
profession                0.123      0.336      0.141        247       5623
worked_at                 0.110      0.479      0.130        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.202      0.439      0.221       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 628 examples
```

Examples of sentences:

```text
'folks pay the bill… so say Angela Merkel and the US Republicans … remember that this autumn when you vote . ______________________________ On Saturday , not only Greece , but also Europe , braced for an election that polls indicated would decimate the two main parties and fail to produce a clear winner , sparking market fears about', 'something to see . Made of polished granite and glass walls it certainly makes quite an impression . This beautiful building showcases an amazing view of the Columbia River Valley , the Cascades and Mt . St. Helens . It is no wonder that this building has received both national and international architectural awards . St. Anne ’ s Chapel This charming little red house once', 'style drew from many sources and transcends any one genre . Their rock-infused interpretation of the blues and folk genres also incorporated rockabilly , reggae , soul , funk , classical , Celtic , Indian , Arabic , pop , Latin and country . The band did not release the popular songs from their', 'are excluded by the dominant aesthetic . For examples of such subversion see : Antonioni , Chaplin , cinematheque , Eisenstein , pornography , Fellini , Godard , Klein , Monroe , underground , Warhol . Every art struggle is a struggle for legitimacy and distinction , and a class will most enthusiastically reject the taste of', 'far his best year , and his stats compare with the best pitchers in baseball . His ERA is 2.72 and his FIP has him behind only Stephen Strasburg and Gio Gonzalez from the Nationals . He ranks 3 rd in WAR behind only Justin Verlander and Felix Hernandez . On average , he is only allowing 1 base-runner to'
```

## With only Science sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.4451328344631092
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.18367831107446178
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.4200982806475336
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.17057799807037458
----BEST SYSTEM----
Best performing system score: 0.4451328344631092
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function directional_bag_of_words_featurizer_original_system at 0x7f57436e67a0>, 'factory_model': <function <lambda> at 0x7f573f3a3a70>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.615      0.488      0.585        340       5716
author                    0.489      0.792      0.530        509       5885
capital                   0.383      0.463      0.396         95       5471
contains                  0.655      0.870      0.689       3904       9280
film_performance          0.570      0.718      0.594        766       6142
founders                  0.399      0.616      0.429        380       5756
genre                     0.265      0.412      0.285        170       5546
has_sibling               0.402      0.661      0.436        499       5875
has_spouse                0.356      0.709      0.395        594       5970
is_a                      0.439      0.541      0.456        497       5873
nationality               0.357      0.688      0.395        301       5677
parents                   0.482      0.689      0.513        312       5688
place_of_birth            0.334      0.554      0.363        233       5609
place_of_death            0.250      0.478      0.276        159       5535
profession                0.363      0.538      0.389        247       5623
worked_at                 0.281      0.471      0.305        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.415      0.605      0.440       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 82,569 examples
```

Examples of sentences:

```text
'7 References 8 External links [ edit ] Victims Christian moved from Louisiana to Tennessee with her family in 1997 . She was a graduate of Farragut High School and a senior majoring in sociology at the University of Tennessee . On January 12 , 2007 , her family released a statement to thank the Knoxville community “ for all their prayers and everything. ” A candlelight vigil was', "know the exact location where my SAYERS family originated in Ireland before they emigrated to Canada in the 1830s . Letterkenny is the largest town in County Donegal , in the province of Ulster , Ireland , and apparently was the home of many Ulster Scots . I 've mentioned before that I really have n't done much Irish research on my family ,", "a few years prior to the opening of his Walt Disney World dream project in Orlando , Florida . Childhood Walt Disney 's ancestors had emigrated from Gowran , County Kilkenny in Ireland . Arundel Elias Disney , great-grandfather of Walt Disney was born in Kilkenny , Ireland in 1801 and was a descendant of Hughes and his", "on the violin , Streep went through two months of intense training , four to six hours a day . [ 51 ] In addition , Streep appeared with Glenn Close in the movie version of Isabel Allende 's The House of the Spirits ; The River Wild ; Marvin 's Room ( with Diane Keaton and Leonardo DiCaprio ) ; and One True Thing . [ edit ] 2000s Main article :", 'Vrana , Romanian painter . Florica Prevenda , Romanian painter Manakis brothers ( Yanaki and Milton Manakia ) , film and photography ; pioneers in the Balkans , from Avdela , Prefecture of Grevena , Macedonia , Greece . * Mihai Tugearu , Romanian sculptor . Papaconstantin Tache , Roumanian Architect , Paris . Stere Gulea , Romanian film maker and Government official . Sultana Maitec , Romanian sculptor . Titi'
```

## With only Politics sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.24948876366353895
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12034177267312561
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.2773979318160761
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12144287375559035
----BEST SYSTEM----
Best performing system score: 0.2773979318160761
{'feauturizer': 'simple_bag_of_words_featurizer', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function simple_bag_of_words_featurizer at 0x7f57b04f2170>, 'factory_model': <function <lambda> at 0x7f57b04f2560>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.053      0.256      0.063        340       5716
author                    0.401      0.709      0.439        509       5885
capital                   0.113      0.263      0.128         95       5471
contains                  0.526      0.665      0.549       3904       9280
film_performance          0.413      0.614      0.442        766       6142
founders                  0.283      0.458      0.307        380       5756
genre                     0.158      0.329      0.177        170       5546
has_sibling               0.151      0.393      0.173        499       5875
has_spouse                0.259      0.579      0.291        594       5970
is_a                      0.310      0.366      0.319        497       5873
nationality               0.278      0.385      0.295        301       5677
parents                   0.323      0.478      0.346        312       5688
place_of_birth            0.159      0.262      0.173        233       5609
place_of_death            0.150      0.302      0.167        159       5535
profession                0.210      0.356      0.228        247       5623
worked_at                 0.164      0.463      0.188        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.247      0.430      0.268       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 2,736 examples
```

Examples of exclamatory sentences:

```text
'choir at age 11 . [ 6 ] After she began performing alongside her mother in night clubs in the New York City area , she was discovered by Arista Records label head Clive Davis . Houston released seven studio albums and three movie soundtrack albums , all of which have diamond , multi-platinum , platinum , or gold certification . Houston was the only', "guitarist for the French Band AIR , ) played an evening of NIck Drake 's songs , narrating and praising Drake 's life story , at Pete 's Candy Store in Brooklyn , New York . I could go on and on about his history but i am sure you got the big picture . He was criticised for not including", "Ray Stevenson ) must band together and defeat the deadly trio of Cardinal Richelieu ( Christoph Waltz ) , the airship inventing Duke of Buckingham ( Orlando Bloom ) and deadly acrobatic assassin Milady de Winter ( Milla Jovovich ) . Yes , seriously . Frankly I 'm both shocked about the liberties taken with the source material , and very worried that impressionable young viewers will watch this", "produced , and stars Max Landis , son of Director John Landis . This hilarious geeked out short film includes celebrity cameos by Elijah Wood , Mandy Moore , Simon Pegg , Jennette McCurdy , and more ! You have to watch this comedic educational fanboy film about how Superman 's death ruined the concept of `` Death '' in", "psychic abilities ; he `` sees dead people , '' and is rather emotionally scarred by this ability . Dean : Hey , Sam , who do you think is a hotter psychic : Patricia Arquette , Jennifer Love Hewitt , or you ? Arquette plays psychic Allison DuBois in the TV series Medium ; Hewitt plays psychic Melinda Gordon in the TV series Ghost Whisperer"
```

## With only Arts sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.49645218100377153
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.19045880638635942
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.48022941550195974
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.18402940642530696
----BEST SYSTEM----
Best performing system score: 0.49645218100377153
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function directional_bag_of_words_featurizer_original_system at 0x7f56eec8d4d0>, 'factory_model': <function <lambda> at 0x7f57814dfa70>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.650      0.497      0.612        340       5716
author                    0.565      0.770      0.597        509       5885
capital                   0.359      0.442      0.373         95       5471
contains                  0.678      0.874      0.709       3904       9280
film_performance          0.586      0.701      0.606        766       6142
founders                  0.464      0.645      0.492        380       5756
genre                     0.259      0.306      0.267        170       5546
has_sibling               0.714      0.200      0.472        499       5875
has_spouse                0.493      0.508      0.496        594       5970
is_a                      0.459      0.493      0.465        497       5873
nationality               0.437      0.684      0.471        301       5677
parents                   0.731      0.506      0.672        312       5688
place_of_birth            0.389      0.476      0.404        233       5609
place_of_death            0.314      0.138      0.251        159       5535
profession                0.414      0.437      0.418        247       5623
worked_at                 0.498      0.426      0.481        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.501      0.507      0.487       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 119,251 examples
```

Examples of sentences:

```text
'Providers Blog Request Information Survey About Contact Swedish Services & Products What Wikipedia says about Portland Portland is a city located in the Northwestern United States , near the confluence of the Willamette and Columbia rivers in the state of Oregon . As of July 2009 , it had an estimated population of 582,130 , [', "whole world is laughing about nazis ) at the anti nazi demonstration `` GrÀfenberg ist bunt '' ( GrÀfenberg is colorful ) at the market place of GrÀfenberg in Upper Franconia ( Bavaria , Germany ) on 18 . August 2007 . Date 18 August 2007 ( 2007-08-18 ) Source own photo taken by Daniel Arnold Author Daniel Arnold Permission", 'hall from the Sunday School classroom . And as for religious imagery , I would probably expect to see something along the lines of Georges Rouault or Marc Chagall but probably not a future Andres Serrano ( even though his Piss Christ makes a profound religious statement ) . But that certainly doesn ’ t mean that art in churches has to be all about sweetness', "in states such as Iowa , Illinois , Indiana , Kentucky , North Carolina , South Carolina , Tennessee , Georgia , Alabama , Mississippi , Louisiana , Texas , Oklahoma and Arkansas . `` Pecan '' is from an Algonquian word ,", 'north , to Ireland in the west , east to Poland and western Russia , [ 15 ] and south throughout the Balkans , in Italy , Spain and Portugal , and in Morocco and Algeria in north Africa . [ 24 ] In west Asia it has been reported from forests of northern Iran . [ 25 ] There'
```

## With only Sports sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.3491694947950328
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12552670543165326
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.3367547630912586
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12250703965158546
----BEST SYSTEM----
Best performing system score: 0.3491694947950328
{'feauturizer': 'directional_bag_of_words_featurizer_original_system', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function directional_bag_of_words_featurizer_original_system at 0x7f56cbd87950>, 'factory_model': <function <lambda> at 0x7f5783b7f320>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.081      0.656      0.099        340       5716
author                    0.453      0.758      0.492        509       5885
capital                   0.103      0.463      0.122         95       5471
contains                  0.632      0.831      0.664       3904       9280
film_performance          0.497      0.636      0.520        766       6142
founders                  0.346      0.618      0.380        380       5756
genre                     0.218      0.335      0.234        170       5546
has_sibling               0.286      0.553      0.317        499       5875
has_spouse                0.328      0.710      0.367        594       5970
is_a                      0.384      0.451      0.395        497       5873
nationality               0.351      0.561      0.380        301       5677
parents                   0.413      0.612      0.442        312       5688
place_of_birth            0.318      0.382      0.329        233       5609
place_of_death            0.194      0.352      0.213        159       5535
profession                0.311      0.482      0.334        247       5623
worked_at                 0.265      0.463      0.290        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.324      0.554      0.349       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 13,756 examples
```

Examples of sentences:

```text
'fur is not especially valuable . Range and habitat The ringtail is found in California , Colorado , eastern Kansas , Oklahoma , Oregon , Arizona , New Mexico , southern Nevada , Texas , Utah and throughout northern and central Mexico . Its distribution overlaps that of B. sumichrasti in the Mexican states of Guerrero , Oaxaca and', 'forms of crown authority , to be replaced by locally created authority . Virginia , South Carolina , and New Jersey created their constitutions before July 4 . Rhode Island and Connecticut simply took their existing royal charters and deleted all references to the crown . [ 56 ] The new states had to decide not only what', 'television and family-friendly comedies before achieving success as a dramatic actor portraying several notable roles , including Andrew Beckett in Philadelphia , the title role in Forrest Gump , Commander James A. Lovell in Apollo 13 , Captain John H. Miller in Saving Private Ryan , Michael Sullivan in Road to Perdition , and Sheriff Woody in Disney', 'made the Fabian Society pre-eminent . Husband of Beatrice Webb ( qv ) . 1859-1940 - George Lansbury - Politician , socialist , Christian pacifist & newspaper editor . P 1860-1926 - Emily Hobhouse - See below . Sister of Leonard Trelawny Hobhouse . Worked with Dame Milicent Fawcett . 1863-1935 - Arthur Henderson - Held many politcal offices . Chaired the Geneva Disarmament Conference in 1932-34 . 1934 1863-1937', 'confused . Here is what Wikipedia had to say about Clear Channel and Bain : Clear Channel Communications , Inc. is an American media conglomerate company headquartered in San Antonio , Texas . [ 3 ] It was founded in 1972 by Lowry Mays and Red McCombs , and was taken private by Bain Capital LLC and Thomas H .'
```

## With only Business sentences in training corpus

### Grid search and results

```text
Experiment # 1
 directional_bag_of_words_featurizer_original_system SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.19526684146986772
Experiment # 2
 directional_bag_of_words_featurizer_original_system NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12363516323097329
Experiment # 3
 simple_bag_of_words_featurizer SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False) 0.22090439824258562
Experiment # 4
 simple_bag_of_words_featurizer NearestCentroid(metric='euclidean', shrink_threshold=None) 0.12300252260366949
----BEST SYSTEM----
Best performing system score: 0.22090439824258562
{'feauturizer': 'simple_bag_of_words_featurizer', 'factory': SGDClassifier(alpha=0.0001, average=False, class_weight=None,
              early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
              l1_ratio=0.15, learning_rate='optimal', loss='hinge',
              max_iter=1000, n_iter_no_change=5, n_jobs=None, penalty='l2',
              power_t=0.5, random_state=None, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False), 'feauturizer_model': <function simple_bag_of_words_featurizer at 0x7f569c2bccb0>, 'factory_model': <function <lambda> at 0x7f5783b7f830>}
relation              precision     recall    f-score    support       size
------------------    ---------  ---------  ---------  ---------  ---------
adjoins                   0.045      0.259      0.054        340       5716
author                    0.230      0.521      0.259        509       5885
capital                   0.065      0.232      0.076         95       5471
contains                  0.504      0.706      0.535       3904       9280
film_performance          0.300      0.431      0.319        766       6142
founders                  0.209      0.295      0.222        380       5756
genre                     0.142      0.265      0.156        170       5546
has_sibling               0.261      0.303      0.269        499       5875
has_spouse                0.220      0.475      0.247        594       5970
is_a                      0.253      0.348      0.268        497       5873
nationality               0.258      0.432      0.281        301       5677
parents                   0.163      0.266      0.177        312       5688
place_of_birth            0.142      0.318      0.160        233       5609
place_of_death            0.132      0.314      0.149        159       5535
profession                0.158      0.340      0.177        247       5623
worked_at                 0.168      0.302      0.185        242       5618
------------------    ---------  ---------  ---------  ---------  ---------
macro-average             0.203      0.363      0.221       9248      95264
```

### Other relevant info

Count of corpus examples:

```text
Corpus pre-filter:  Corpus with 266,759 examples
Corpus post-filter:  Corpus with 727 examples
```

Examples of sentences:

```text
"Petaluma , offered a $ 200,000 reward for her safe return during the search for Polly Klaas ; after Klaas ' death , Ryder starred in a film version of Little Women and dedicated it to Klaas ' memory , the Louisa May Alcott novel having been Polly 's favorite book . The producers at first wanted to remove the dedication . Ryder then said she would not do any publicity for", 'Baart de la Faille ( 1970 ( 1970 ) ) [ 1928 ( 1928 ) ] The Works of Vincent van Gogh . His Paintings and Drawings . , Amsterdam : J.M . Meulenhoff , no . 646 . JH1686 : Jan Hulsker ( 1980 ) , The Complete Van Gogh , Oxford : Phaidon , no . 1686 . Source/Photographer repro from artbook Permission ( Reusing this file ) Public domain Public domain false', 'shirts , but she ’ s also a big Air Jordan / sneakerhead ! She also loves joking around , Jay-Z , Kanye , The Dream , Jeezy , Trey Songz , Eric Benet and Bobby Valentino just to name a few . It ’ s fans like Ericka that help motivate me to constantly make FFB EVEN better . And the pressure ’ s on , because I', 'somewhat after the latter . [ 9 ] His television career bloomed with , as well as Manimal , parts in series such as Dynasty , Fantasy Island , Hart to Hart , Matt Houston and The Dukes of Hazzard . [ 9 ] [ 8 ] [ 2 ] He also played David Clement , an aristocrat , in the mini-series Manions of America . [ 8 ] [ 2 ]', 'to account . On Al Jazeera English . Al Jazeera English ( AJE ) is a 24-hour English -language news and current affairs TV channel headquartered in Doha , Qatar . It is the sister channel of the Arabic-language Al Jazeera . The budget debate and the economy are the battleground on which the 2012 presidential election race will be fought . And the US has never']
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
