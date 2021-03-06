#!/usr/bin/env python
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for google_vision_api_text_detect."""

import pytest

import google_vision_api_text_detect


class TestBatch:
    def test_empty(self):
        for batch_size in range(1, 10):
            assert len(list(google_vision_api_text_detect.batch([], batch_size=batch_size))) == 0

    def test_single(self):
        for batch_size in range(1, 10):
            batched = tuple(google_vision_api_text_detect.batch([1], batch_size=batch_size))
            assert batched == ((1,),)

    def test_no_remainders(self):
        batched = tuple(google_vision_api_text_detect.batch([1, 2], batch_size=2))
        assert batched == ((1, 2),)
        batched = tuple(google_vision_api_text_detect.batch([1, 2, 3], batch_size=3))
        assert batched == ((1, 2, 3),)
        batched = tuple(google_vision_api_text_detect.batch([1, 2, 3, 4], batch_size=2))
        assert batched == ((1, 2), (3, 4))
        batched = tuple(google_vision_api_text_detect.batch([1, 2, 3, 4, 5, 6], batch_size=3))
        assert batched == ((1, 2, 3), (4, 5, 6))

    def test_remainders(self):
        batched = tuple(google_vision_api_text_detect.batch([1, 2], batch_size=3))
        assert batched == ((1, 2,),)
        batched = tuple(google_vision_api_text_detect.batch([1, 2, 3], batch_size=2))
        assert batched == ((1, 2), (3,))
        batched = tuple(google_vision_api_text_detect.batch([1, 2, 3, 4], batch_size=3))
        assert batched == ((1, 2, 3), (4,))
        batched = tuple(google_vision_api_text_detect.batch([1, 2, 3, 4, 5], batch_size=3))
        assert batched == ((1, 2, 3), (4, 5))
        batched = tuple(google_vision_api_text_detect.batch([1, 2, 3, 4, 5], batch_size=4))
        assert batched == ((1, 2, 3, 4), (5,))


class TestDetectText:
    def test_single_image_returns_text(self):
        vision = google_vision_api_text_detect.VisionApi()

        texts = vision.detect_text(["img/text/wakeupcat.jpg"])

        assert "img/text/wakeupcat.jpg" in texts
        document = google_vision_api_text_detect.extract_description(
                texts["img/text/wakeupcat.jpg"]).lower()
        assert "wake" in document
        assert "up" in document
        assert "human" in document

    def test_single_nonimage_returns_error(self):
        vision = google_vision_api_text_detect.VisionApi()
        texts = vision.detect_text(["img/text/not-a-meme.txt"])
        assert "img/text/not-a-meme.txt" not in texts

    def test_batch_images_returns_text(self):
        vision = google_vision_api_text_detect.VisionApi()

        texts = vision.detect_text([
                "img/text/wakeupcat.jpg",
                "img/text/bonito.gif",
        ])

        assert "img/text/wakeupcat.jpg" in texts
        wakeupcat = google_vision_api_text_detect.extract_description(
                texts["img/text/wakeupcat.jpg"]).lower()
        assert "wake" in wakeupcat
        assert "up" in wakeupcat
        assert "human" in wakeupcat
        assert "img/text/bonito.gif" in texts
        bonito = google_vision_api_text_detect.extract_description(
                texts["img/text/bonito.gif"]).lower()
        assert "bonito" in bonito
        assert "fermented" in bonito

    def test_batch_mixed_returns_partialsuccess(self):
        vision = google_vision_api_text_detect.VisionApi()
        texts = vision.detect_text([
                "img/text/wakeupcat.jpg",
                "img/text/not-a-meme.txt"
        ])
        assert "img/text/wakeupcat.jpg" in texts
        assert "img/text/not-a-meme.txt" not in texts


if __name__ == '__main__':
    pytest.main()

