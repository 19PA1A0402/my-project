{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled8.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/19PA1A0402/my-project/blob/master/NLTK..REGEX.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lipUlmT96xvB"
      },
      "source": [
        "text1 =\"i am here\""
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jZo3gUDU63Ka",
        "outputId": "70befebe-6bfa-4789-f7b0-45b6904898b5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "len(text1)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "9"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-9q5bcB87PlF",
        "outputId": "6bec235a-3680-4f60-ba9e-33d34083b2c7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "text2 = text1.split()\n",
        "text2"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['i', 'am', 'here']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lLir92qc7PzS",
        "outputId": "42f26b1d-ff34-483d-9531-1e7f86477092",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "[w for w in text2 if w.endswith(\"e\")]"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['here']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yEFIEDRM_6-g"
      },
      "source": [
        "import re"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QJqizWLzAGm0"
      },
      "source": [
        "text3= \"this is text with #hashtag @callout\""
      ],
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BZlPJlFvBEvU",
        "outputId": "4c7d1cb5-b2a0-4529-b238-fd5797bd6a25",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "text4=text3.split()\n",
        "text4"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['this', 'is', 'text', 'with', '#hashtag', '@callout']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4EC1MR4GBO1H",
        "outputId": "39082fc6-f87b-437b-b1fd-595554697e28",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "print([w for w in text4 if re.search('@[A-Za-z0-9]+',w)])\n",
        "print(re.findall(r'[aeiou]',text3))\n",
        "re.findall(r'[^aeiou]',text3)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "['@callout']\n",
            "['i', 'i', 'e', 'i', 'a', 'a', 'a', 'o', 'u']\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['t',\n",
              " 'h',\n",
              " 's',\n",
              " ' ',\n",
              " 's',\n",
              " ' ',\n",
              " 't',\n",
              " 'x',\n",
              " 't',\n",
              " ' ',\n",
              " 'w',\n",
              " 't',\n",
              " 'h',\n",
              " ' ',\n",
              " '#',\n",
              " 'h',\n",
              " 's',\n",
              " 'h',\n",
              " 't',\n",
              " 'g',\n",
              " ' ',\n",
              " '@',\n",
              " 'c',\n",
              " 'l',\n",
              " 'l',\n",
              " 't']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "psNmKOCoFZVp"
      },
      "source": [
        "datestr = \"28-10-2020/28/10/20/28oct20/28oct2020/n28-10-2020\""
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GzZ6Bu4sHIec",
        "outputId": "f7e5f84d-743b-4409-bc69-5f49f5b9bfa6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "re.findall(r'[d{2}[/-]d{2}[/-]d{2}]',datestr)"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Mj1dA7tsKnAH",
        "outputId": "773bdea5-0b0c-4b99-cff7-078513774fd0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "!pip install nltk"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: nltk in /usr/local/lib/python3.6/dist-packages (3.2.5)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.6/dist-packages (from nltk) (1.15.0)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PhKEZSp1I-A8"
      },
      "source": [
        "import nltk"
      ],
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "amxgrWPkLfNY",
        "outputId": "0ce7252c-96e7-401a-bd63-316aff7a9f28",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "nltk.download()"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "NLTK Downloader\n",
            "---------------------------------------------------------------------------\n",
            "    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit\n",
            "---------------------------------------------------------------------------\n",
            "Downloader> d\n",
            "\n",
            "Download which package (l=list; x=cancel)?\n",
            "  Identifier> book\n",
            "    Downloading collection 'book'\n",
            "       | \n",
            "       | Downloading package abc to /root/nltk_data...\n",
            "       |   Unzipping corpora/abc.zip.\n",
            "       | Downloading package brown to /root/nltk_data...\n",
            "       |   Unzipping corpora/brown.zip.\n",
            "       | Downloading package chat80 to /root/nltk_data...\n",
            "       |   Unzipping corpora/chat80.zip.\n",
            "       | Downloading package cmudict to /root/nltk_data...\n",
            "       |   Unzipping corpora/cmudict.zip.\n",
            "       | Downloading package conll2000 to /root/nltk_data...\n",
            "       |   Unzipping corpora/conll2000.zip.\n",
            "       | Downloading package conll2002 to /root/nltk_data...\n",
            "       |   Unzipping corpora/conll2002.zip.\n",
            "       | Downloading package dependency_treebank to /root/nltk_data...\n",
            "       |   Unzipping corpora/dependency_treebank.zip.\n",
            "       | Downloading package genesis to /root/nltk_data...\n",
            "       |   Unzipping corpora/genesis.zip.\n",
            "       | Downloading package gutenberg to /root/nltk_data...\n",
            "       |   Unzipping corpora/gutenberg.zip.\n",
            "       | Downloading package ieer to /root/nltk_data...\n",
            "       |   Unzipping corpora/ieer.zip.\n",
            "       | Downloading package inaugural to /root/nltk_data...\n",
            "       |   Unzipping corpora/inaugural.zip.\n",
            "       | Downloading package movie_reviews to /root/nltk_data...\n",
            "       |   Unzipping corpora/movie_reviews.zip.\n",
            "       | Downloading package nps_chat to /root/nltk_data...\n",
            "       |   Unzipping corpora/nps_chat.zip.\n",
            "       | Downloading package names to /root/nltk_data...\n",
            "       |   Unzipping corpora/names.zip.\n",
            "       | Downloading package ppattach to /root/nltk_data...\n",
            "       |   Unzipping corpora/ppattach.zip.\n",
            "       | Downloading package reuters to /root/nltk_data...\n",
            "       | Downloading package senseval to /root/nltk_data...\n",
            "       |   Unzipping corpora/senseval.zip.\n",
            "       | Downloading package state_union to /root/nltk_data...\n",
            "       |   Unzipping corpora/state_union.zip.\n",
            "       | Downloading package stopwords to /root/nltk_data...\n",
            "       |   Unzipping corpora/stopwords.zip.\n",
            "       | Downloading package swadesh to /root/nltk_data...\n",
            "       |   Unzipping corpora/swadesh.zip.\n",
            "       | Downloading package timit to /root/nltk_data...\n",
            "       |   Unzipping corpora/timit.zip.\n",
            "       | Downloading package treebank to /root/nltk_data...\n",
            "       |   Unzipping corpora/treebank.zip.\n",
            "       | Downloading package toolbox to /root/nltk_data...\n",
            "       |   Unzipping corpora/toolbox.zip.\n",
            "       | Downloading package udhr to /root/nltk_data...\n",
            "       |   Unzipping corpora/udhr.zip.\n",
            "       | Downloading package udhr2 to /root/nltk_data...\n",
            "       |   Unzipping corpora/udhr2.zip.\n",
            "       | Downloading package unicode_samples to /root/nltk_data...\n",
            "       |   Unzipping corpora/unicode_samples.zip.\n",
            "       | Downloading package webtext to /root/nltk_data...\n",
            "       |   Unzipping corpora/webtext.zip.\n",
            "       | Downloading package wordnet to /root/nltk_data...\n",
            "       |   Unzipping corpora/wordnet.zip.\n",
            "       | Downloading package wordnet_ic to /root/nltk_data...\n",
            "       |   Unzipping corpora/wordnet_ic.zip.\n",
            "       | Downloading package words to /root/nltk_data...\n",
            "       |   Unzipping corpora/words.zip.\n",
            "       | Downloading package maxent_treebank_pos_tagger to\n",
            "       |     /root/nltk_data...\n",
            "       |   Unzipping taggers/maxent_treebank_pos_tagger.zip.\n",
            "       | Downloading package maxent_ne_chunker to /root/nltk_data...\n",
            "       |   Unzipping chunkers/maxent_ne_chunker.zip.\n",
            "       | Downloading package universal_tagset to /root/nltk_data...\n",
            "       |   Unzipping taggers/universal_tagset.zip.\n",
            "       | Downloading package punkt to /root/nltk_data...\n",
            "       |   Unzipping tokenizers/punkt.zip.\n",
            "       | Downloading package book_grammars to /root/nltk_data...\n",
            "       |   Unzipping grammars/book_grammars.zip.\n",
            "       | Downloading package city_database to /root/nltk_data...\n",
            "       |   Unzipping corpora/city_database.zip.\n",
            "       | Downloading package tagsets to /root/nltk_data...\n",
            "       |   Unzipping help/tagsets.zip.\n",
            "       | Downloading package panlex_swadesh to /root/nltk_data...\n",
            "       | Downloading package averaged_perceptron_tagger to\n",
            "       |     /root/nltk_data...\n",
            "       |   Unzipping taggers/averaged_perceptron_tagger.zip.\n",
            "       | \n",
            "     Done downloading collection book\n",
            "\n",
            "---------------------------------------------------------------------------\n",
            "    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit\n",
            "---------------------------------------------------------------------------\n",
            "Downloader> q\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pARclAUuLrPk"
      },
      "source": [
        "from nltk.book import *"
      ],
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1Kk__TW-MGSG",
        "outputId": "b9c6d0fd-fd1c-4f4a-df5f-a73f09a9e0b5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "type(text1)"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "nltk.text.Text"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2wDrojziMLhB",
        "outputId": "9ae6db2a-1078-464b-e9df-9e3912f4c460",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "sents()"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "sent1: Call me Ishmael .\n",
            "sent2: The family of Dashwood had long been settled in Sussex .\n",
            "sent3: In the beginning God created the heaven and the earth .\n",
            "sent4: Fellow - Citizens of the Senate and of the House of Representatives :\n",
            "sent5: I have a problem with people PMing me to lol JOIN\n",
            "sent6: SCENE 1 : [ wind ] [ clop clop clop ] KING ARTHUR : Whoa there !\n",
            "sent7: Pierre Vinken , 61 years old , will join the board as a nonexecutive director Nov. 29 .\n",
            "sent8: 25 SEXY MALE , seeks attrac older single lady , for discreet encounters .\n",
            "sent9: THE suburb of Saffron Park lay on the sunset side of London , as red and ragged as a cloud of sunset .\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pmgTfk5-0cZQ",
        "outputId": "a46bb26b-f8b0-4356-953a-c74a0bd7d571",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "sent1"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Call', 'me', 'Ishmael', '.']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lzfrE1ATCY04",
        "outputId": "16570822-ff23-401e-e761-279539b26740",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "text1"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Text: Moby Dick by Herman Melville 1851>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VWWLpmDPC9Rn",
        "outputId": "3ee3fc3e-511c-4baf-a59e-170e7f5f0bed",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "len(text7)"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "100676"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zDQdQjE7DGnC",
        "outputId": "9811039e-acea-4898-856f-aa5e774ffa3d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "len(set(text7))"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "12408"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tr43exigDgCg",
        "outputId": "5cd0c588-30d4-4227-9681-ce9e99dab7f6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "len(text7)/len(set(text7))"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "8.113797549967762"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "horuCYUaD2uN",
        "outputId": "5c4dcafc-566f-4ca1-d4ce-6a77747de6e6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "list(set(text7))[1:10]"
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['suspensions',\n",
              " 'DiLoreto',\n",
              " 'parts-engineering',\n",
              " 'cloth',\n",
              " 'Eugene',\n",
              " 'instead',\n",
              " 'knell',\n",
              " 'Larry',\n",
              " 'positions']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vABt1-KAEtPc"
      },
      "source": [
        "dist = FreqDist(text7)"
      ],
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eyOxk1vuFFgH",
        "outputId": "b1899d3f-e5ff-4a6d-db9e-8300f58388c6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "len(dist)"
      ],
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "12408"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4-wyfyKHFQWd"
      },
      "source": [
        "vocabulary=dist.keys()\n"
      ],
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aVhIOkw_GJft",
        "outputId": "7ee87a58-ec87-4a43-a885-0bd7ce902a73",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "list(vocabulary)[:10]"
      ],
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Pierre', 'Vinken', ',', '61', 'years', 'old', 'will', 'join', 'the', 'board']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Y9GnaqXMGT1E",
        "outputId": "a443fb83-91dc-46ad-93ca-d2df3479e277",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "dist['old']"
      ],
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "24"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1F02U6V9G3f6",
        "outputId": "b48d3a4f-9a4a-4bbd-9564-aa964babe1df",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 288
        }
      },
      "source": [
        "#frequency distribution plot\n",
        "import matplotlib.pyplot as plt\n",
        "dist.plot(10,cumulative=False)\n",
        "plt.show()"
      ],
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WyV0AZtCIi3r"
      },
      "source": [
        "### *Fine-grained selection of words*"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1ekBzAhaIL8N",
        "outputId": "822402b1-96f3-4fee-b09c-ab0030998231",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "freqwords = [w for w in vocabulary if len(w)>5 and dist[w]>100]\n",
        "freqwords"
      ],
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['billion',\n",
              " 'company',\n",
              " 'president',\n",
              " 'because',\n",
              " 'market',\n",
              " 'million',\n",
              " 'shares',\n",
              " 'trading',\n",
              " 'program']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 70
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oXzyhBDyJuG9"
      },
      "source": [
        "Normalization and Stemming"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XVKM5yaNJ3AW",
        "outputId": "2874d625-498e-44f2-af7f-d9f268e19c1d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "input1 = \"List listed lists listing listings\"\n",
        "words1 = input1.lower().split(' ')\n",
        "words1"
      ],
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['list', 'listed', 'lists', 'listing', 'listings']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 74
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xv9EkQhjLwzH",
        "outputId": "44f13f58-c375-4929-b13c-1aca6a700914",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "porter = nltk.PorterStemmer()\n",
        "[porter.stem(t) for t in words1]"
      ],
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['list', 'list', 'list', 'list', 'list']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 75
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fWHGlSxDNG_4"
      },
      "source": [
        "Lemmatisation"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XjN5tluFNKGd",
        "outputId": "691e96c3-790e-4f06-f041-f5ff7751a45c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "udhr =nltk.corpus.udhr.words('English-Latin1')\n",
        "udhr[:20]"
      ],
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Universal',\n",
              " 'Declaration',\n",
              " 'of',\n",
              " 'Human',\n",
              " 'Rights',\n",
              " 'Preamble',\n",
              " 'Whereas',\n",
              " 'recognition',\n",
              " 'of',\n",
              " 'the',\n",
              " 'inherent',\n",
              " 'dignity',\n",
              " 'and',\n",
              " 'of',\n",
              " 'the',\n",
              " 'equal',\n",
              " 'and',\n",
              " 'inalienable',\n",
              " 'rights',\n",
              " 'of']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 76
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eFXCanGVPRJa",
        "outputId": "a2bbe750-b1c3-4e1b-b68c-de24e62739d7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "[porter.stem(t) for t in udhr[:20]]"
      ],
      "execution_count": 79,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['univers',\n",
              " 'declar',\n",
              " 'of',\n",
              " 'human',\n",
              " 'right',\n",
              " 'preambl',\n",
              " 'wherea',\n",
              " 'recognit',\n",
              " 'of',\n",
              " 'the',\n",
              " 'inher',\n",
              " 'digniti',\n",
              " 'and',\n",
              " 'of',\n",
              " 'the',\n",
              " 'equal',\n",
              " 'and',\n",
              " 'inalien',\n",
              " 'right',\n",
              " 'of']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 79
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BKjexeSTQRf5"
      },
      "source": [
        "Word Net Lemmatization"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_cZxC7AWQQXr",
        "outputId": "4cffd9fa-e6e0-4e13-856e-83277929ec60",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "WNlemma = nltk.WordNetLemmatizer()\n",
        "[WNlemma.lemmatize(t) for t in udhr[:10]]"
      ],
      "execution_count": 83,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Universal',\n",
              " 'Declaration',\n",
              " 'of',\n",
              " 'Human',\n",
              " 'Rights',\n",
              " 'Preamble',\n",
              " 'Whereas',\n",
              " 'recognition',\n",
              " 'of',\n",
              " 'the']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 83
        }
      ]
    }
  ]
}