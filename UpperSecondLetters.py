{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOb1/kaqfqmqv+XbF06Br+V",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/1slewis/testing-python/blob/main/UpperSecondLetters.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "string = \"this has more features!\"\n",
        "\n",
        "skipCharacters = [\" \",\"!\"]\n",
        "\n",
        "chars = list(string)\n",
        "\n",
        "def toTitle(input):\n",
        "  output = \"\"\n",
        "  i = -1\n",
        "  diff = 0\n",
        "  while i < (len(input) - 1):\n",
        "    i += 1\n",
        "    ifCont = False\n",
        "    for exception in skipCharacters:\n",
        "      if(input[i] == exception):\n",
        "       diff += 1\n",
        "       output += exception\n",
        "       ifCont = True\n",
        "    if (ifCont): \n",
        "      continue\n",
        "    if ((i - diff) % 2):\n",
        "      output += input[i].upper()\n",
        "      continue\n",
        "    if not((i - diff) % 2):\n",
        "      output += input[i].lower()\n",
        "      continue\n",
        "  return(output)\n",
        "\n",
        "print(toTitle(string))\n",
        "print(toTitle(chars))"
      ],
      "metadata": {
        "id": "OZAoIEvNYUsB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "181e0c1a-4e33-4a4e-af64-ca887c4db1be"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "tHiS hAs MoRe FeAtUrEs!\n",
            "tHiS hAs MoRe FeAtUrEs!\n"
          ]
        }
      ]
    }
  ]
}