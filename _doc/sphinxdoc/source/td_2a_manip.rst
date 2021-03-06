
.. _l-td2a-manip:

========================
Agilité avec les données
========================

Faire du machine learning veut d'abord dire
être capable de manipuler les données comme bon vous semble
et les représenter à l'aide de graphiques.

.. contents::
    :local:

.. |pyecopng| image:: _static/pyeco.png
            :height: 20
            :alt: Economie
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: _static/pystat.png
            :height: 20
            :alt: Statistique
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

------------

|pyecopng|

Rappels de programmation
========================

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/td2_eco_rappels_1a

.. index:: sérialisation, index, dataframe

------------

Matrices et DataFrames - numpy pandas SQL
=========================================

Import/export de données dans un DataFrame,
manipulation selon une logique SQL,
utilité des index,
`lambda function <http://www.diveintopython.net/power_of_introspection/lambda_functions.html>`_,
premiers graphiques,
commandes magiques.

.. contents::
    :local:
    :depth: 1

De nombreux livres ont été écrits sur la manipulation des données en :epkg:`Python`. En voici un :
`Python Data Science Handbook <https://github.com/jakevdp/PythonDataScienceHandbook>`_.

|pyecopng| |pystatpng|

DataFrame
+++++++++

*Notebooks*

.. toctree::
    :maxdepth: 1

    notebooks/td2a_cenonce_session_1
    notebooks/td2a_correction_session_1
    notebooks/pandas_iterator
    notebooks/pandas_iterator_correction
    notebooks/td2a_eco_exercices_de_manipulation_de_donnees
    notebooks/td2a_eco_exercices_de_manipulation_de_donnees_correction_a
    notebooks/td2a_eco_exercices_de_manipulation_de_donnees_correction_b
    notebooks/td2a_eco_exercices_de_manipulation_de_donnees_correction_c

*Modules*

* `pandas <http://pandas.pydata.org/>`_

|pyecopng| |pystatpng|

Array, Matrix
+++++++++++++

*Notebooks*

.. toctree::
    :maxdepth: 1

    notebooks/td2a_cenonce_session_2A
    notebooks/td2a_correction_session_2A

*Lectures*

* `From Python to Numpy <http://www.labri.fr/perso/nrougier/from-python-to-numpy/>`_

*Modules*

* `numpy <http://www.numpy.org/>`_
* `scipy <https://www.scipy.org/>`_

|pyecopng| |pystatpng|

SQL
+++

.. toctree::
    :maxdepth: 1

    ext2a/sql_doc
    questions/sql_reperes

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_sql

.. _l-visualisation-td2a:

------------

Visualisation
=============

.. contents::
    :local:
    :depth: 1

|pyecopng| |pystatpng|

Graphes
+++++++

Il existe de nombreuses librairies de visualisation réparties en deux grandes familles.
La première produit des images
(`matplotlib <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_matplotlib.html#immatplotlibrst>`_,
`seaborn <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_seaborn.html#imseabornrst>`_,
`networkx <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_networkx.html#imnetworkxrst>`_),
la seconde produit des graphes animés à l'aide de Javascript
(`bokeh <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/js_bokeh.html#jsbokehrst>`_,
`bqplot <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_networkx.html#imnetworkxrst>`_).
Les librairies les plus récentes implémentent les deux modes en cherchant toujours plus
de simplicité. A ce sujet, il faut jeter un coup d'oeil à
`flexx <https://flexx.readthedocs.io/en/stable/>`_. Elles explorent aussi
la visualisation animée de gros jeux de données telle que
`datashader <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/big_datashader.html#bigdatashaderrst>`_.

*Notebook sur matplotlib*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_visu

* `Graphes classiques métriques pour des modèles de machine learning <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_ml_enonce.html>`_
* `Graphes classiques métriques pour des modèles de machine learning - correction <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_ml_correction.html>`_

*Notebook sur Javascript*

.. toctree::
    :maxdepth: 2

    ext2a/javascript_doc

* Lire :ref:`Javascript et traitement de données <blog-js-data>`

*Lectures*

* `10 plotting libraries at PyData 2016 <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_

*Modules*

* `matplotlib <http://matplotlib.org/>`_
* `seaborn <https://github.com/mwaskom/seaborn>`_
* `bokeh <http://bokeh.pydata.org/en/latest/>`_
* `bqplot <https://github.com/bloomberg/bqplot>`_
* :ref:`l-visualisation`

*Modules Notebooks*

* `clustergrammer-widget <https://github.com/MaayanLab/clustergrammer-widget>`_ :
  widget pour les notebooks
* `Jupyter Dashboards Layout Extension <http://jupyter-dashboards-layout.readthedocs.io/en/latest/>`_
* `visJS2jupyter <https://ucsd-ccbb.github.io/visJS2jupyter/>`_ : représentation
  de réseaux avec `vis.js <http://visjs.org/>`_
* `neo4jupyter <https://github.com/merqurio/neo4jupyter>`_ :
  `Neo4j <https://neo4j.com/>`_ dans un notebook
* `ipyvolume <https://github.com/maartenbreddels/ipyvolume>`_

|pyecopng| |pystatpng|

.. _l-py2a-cartes:

Cartes
++++++

*Notebooks*

* :ref:`td1acenoncesession12rst`
* :ref:`td1acorrectionsession12rst`
* `Evolution d'une population <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance4_projection_population_enonce.html>`_
* `Evolution d'une population - correction <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_correction.html>`_

*Formats de données*

* :ref:`Système de coordonnées <blog-donnees-carroyees-2016>` (et données carroyées)
* format de cartes
  `shapefiles <https://en.wikipedia.org/wiki/Shapefile>`_,
  `topoJSON <https://en.wikipedia.org/wiki/GeoJSON#TopoJSON>`_,
  `geoJSON <https://en.wikipedia.org/wiki/GeoJSON>`_,
* `Projections sphériques et conversion <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/notebooks/chsh_geo.html>`_
* conversion de coordonnées en longitude / latitude
* librairies
  `basemap <http://matplotlib.org/basemap/>`_, ...
* sources :
  `DataMaps <http://datamaps.github.io/>`_,
  `Find Data <https://bost.ocks.org/mike/map/#finding-data>`_

*Modules*

* `cartopy <http://scitools.org.uk/cartopy/>`_
* `pyshp <https://pypi.python.org/pypi/pyshp>`_
* `shapely <https://pypi.python.org/pypi/Shapely>`_
* `pyproj <https://pypi.python.org/pypi/pyproj>`_
* `geopy <https://pypi.python.org/pypi/geopy>`_
* `basemap <http://matplotlib.org/basemap/>`_
  (maintenu jusqu'en 2020, il faut préférer `cartopy <http://scitools.org.uk/cartopy/>`_)
* `geoviews <http://geo.holoviews.org/Geometries.html>`_

*Modules avec Open Street Map*

* `ipyleaflet <https://github.com/ellisonbg/ipyleaflet>`_
* `folium <https://github.com/python-visualization/folium>`_

|pyecopng| |pystatpng|

Graphes pour des statisticiens
++++++++++++++++++++++++++++++

(*à venir*)

*Lectures*

* `Maximum & Fast readability of multivariate data vs Label <https://medium.com/data-design/maximum-fast-readability-of-multivariate-data-vs-label-c500572c46d1>`_

*Modules*

* `seaborn <https://seaborn.pydata.org/>`_
* `statsmodels <http://www.statsmodels.org/stable/index.html>`_

|pystatpng|

Visualiser pour comprendre
++++++++++++++++++++++++++

(*à venir*)

*Lectures*

* `Towards Reliable Interactive Data Cleaning: A User Survey and Recommendations <http://sirrice.github.io/files/papers/cleaning-hilda16.pdf>`_
* `Combining Design and Performance in aData Visualization Management System <https://www.dropbox.com/s/0rdjsv7m7wbhmlk/cidr17-camera.pdf?dl=0>`_

*Modules*

* `TensorBoard <https://www.tensorflow.org/versions/r0.12/tutorials/>`_ : c'est un projet qui risque de prendre pas mal d'ampleur.
  Il sert à visualiser les résultats intermédiaires, à comparer, à voir les résultats d'un processus
  de machine learning, en particulier les réseaux de neurones profond. Même `Keras <https://keras.io/callbacks/#tensorboard>`_ s'y met.
  `How to use tensorboard Embedding Projector ? <http://stackoverflow.com/questions/40849116/how-to-use-tensorboard-embedding-projector/42775951>`_
  Exemples `TensorBoard: Embedding Visualization <http://ahogrammer.com/2016/12/01/tensorboard-embedding-visualization/>`_,
  `An Encounter with Google’s TensorFlow <https://esciencegroup.com/2016/01/05/an-encounter-with-googles-tensorflow/>`_,
  `How to plot a ROC curve with Tensorflow and scikit-learn? <http://stackoverflow.com/questions/36939328/how-to-plot-a-roc-curve-with-tensorflow-and-scikit-learn>`_
* `Prodigy <https://prodi.gy/>`_ : les problèmes d'apprentissage supervisés requiert des
  annotations ou labels. Il est plus facile de les produire avec de bons outils.
  `Prodigy <https://prodi.gy/>`_ pourrait être l'un d'eux, l'outil est prévu
  pour annoter le texte et les images.
* `labelImg <https://github.com/tzutalin/labelImg>`_ : annotation d'images

------------

Pipelines
=========

.. contents::
    :local:
    :depth: 1

|pyecopng| |pystatpng|

Séquence de traitemements de données
++++++++++++++++++++++++++++++++++++

Il est très rare qu'un modèle de machine learning puisse
être appliqué sur des données brutes. Il y a toujours
une étape de nettoyages, de traitements des valeurs manquantes.
Ce sont souvent des étapes qu'on effectue dans plusieurs cellules
distinctes d'un notebook et qu'on exécute à chaque fois
que les données sont rafraîchies. On peut néanmoins vouloir
les assembler en un seul objet afin de simplifier le code,
on peut aussi souhaiter optimiser certains paramètres, un
traitement particulier au sein d'une séquence de traitements.
C'est ainsi que la notion de *pipeline*, c'est un objet
qui conserve la mémoire d'une séquence de traitements
tout en lui donnant l'apparence d'un seul.

(*à venir*)

*Lecture*

* `Pipeline <http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline>`_
* `FeatureUnion <http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion>`_
* `FunctionTransformer <http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer>`_
* `ItemSelector <http://scikit-learn.org/stable/auto_examples/hetero_feature_union.html>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/>`_

|pystatpng|

Workflows - Data Pipelines
++++++++++++++++++++++++++

Au fur et à mesure qu'une société construire des modèles
de machine learning pour automatiser certaines parties de
traitement de données, il devient important de rafraîchir
ces modèles avec des données plus récentes. On se retrouve vite
avec une multitud de besoins comme automatiser,
garder la trace des précédentes exécutions,
paralléliser sur plusieurs machines ou infrastructures,
garder une vue exhaustive et simple de toute cette complexité
croissante. La dénomination communue est *pipeline* ou
*workflow* et cet ensemble de traitements est souvent
représenté sous formes de graphe où chaque arc
symbolise une dépendances entre deux traitements de données.
Chaque société a développé ses propres outils,
certaines l'ont mis à disposition de façon open source.
Cette partie vise à présenter l'une d'entre elles.

(*à venir*)

*Lectures*

* `Luigi vs Airflow vs Pinball <http://bytepawn.com/luigi-airflow-pinball.html>`_
* `Luigi vs Airflow vs zope.wfmc: Comparison of Open-Source Workflow Engines <https://medium.com/@cyrusv/luigi-vs-airflow-vs-zope-wfmc-comparison-of-open-source-workflow-engines-de5209e6dac1>`_
* `Airflow Tutorial for Data Pipelines <https://blog.godatadriven.com/practical-airflow-tutorial>`_

*Modules*

* `airflow <https://airflow.apache.org/>`_
* `luigi <https://github.com/spotify/luigi>`_
* `pinball <https://github.com/pinterest/pinball>`_
