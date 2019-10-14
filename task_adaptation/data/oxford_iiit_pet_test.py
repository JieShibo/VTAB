# coding=utf-8
# Copyright 2019 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for oxford_iiit_pet.py."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from task_adaptation.data import data_testing_lib
from task_adaptation.data import oxford_iiit_pet
import tensorflow as tf


class OxfordIIITPetDataTest(data_testing_lib.BaseTfdsDataTest):
  """See base class for usage and test descriptions."""

  def setUp(self):
    super(OxfordIIITPetDataTest, self).setUp(
        data_wrapper=oxford_iiit_pet.OxfordIIITPetData(),
        num_classes=37,
        expected_num_samples=dict(
            train=2944,
            val=736,
            trainval=3680,
            test=3669,
        ),
        required_tensors_shapes={
            "image": (None, None, 3),
            "label": (),
        })


if __name__ == "__main__":
  tf.test.main()
