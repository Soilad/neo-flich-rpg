from classes import Room, Obj, Portal, Chaser, cwd, Trader

levels = [
    Room(
        "flichroom",
        "I_forgor_my_wallet",
        1,
        [
            Obj(
                f"{cwd}/rooms/flichroom/objects/bed.png",
                (510, 357),
                [{("Sigil of Dormancy", -1): 3}],
                [
                    [
                        (("sawman", "ono"), "my beautiful body pillow"),
                        (
                            ("sawman", "woe"),
                            "my girlfried isnt a lot to touch her",
                        ),
                    ],
                ],
            ),
            Obj(
                f"{cwd}/rooms/flichroom/objects/pianoooo.png",
                (670, 400),
                [{("Sigil of Friendship", -1): 3}],
                [
                    [
                        (("sawman", "ono"), "a four man piano"),
                        (
                            ("sawman", "woe"),
                            "bought it frm my clones",
                        ),
                        (
                            ("sawman", "woe"),
                            "i barely touch ts i use arch",
                        ),
                    ],
                    [
                        (("zweistein", "sad"), "why tf did u give us okarun's balls"),
                        (
                            0,
                            "its gonna take me years to castrate someone with no balls so take this and leave",
                        ),
                        (("sawman", "ono"), "..."),
                        (("sawman", "sad"), "jesus"),
                    ],
                ],
            ),
            Obj(
                f"{cwd}/rooms/flichroom/objects/famoly.png",
                (874, 219),
                [{("Sigil of Friendship", -1): 3}],
                [
                    [
                        (("sawman", "ono"), "NO WAY?!?!?!?"),
                        (("zweistein", "sad"), "is that the michael bed"),
                        (
                            0,
                            "ihaveseencrimesbeyondanyonespossibilitieswithinthesewalls",
                        ),
                        (
                            ("sawman", "woe"),
                            "...",
                        ),
                        (
                            ("zweistein", "sad"),
                            "skill issue",
                        ),
                    ],
                    [
                        (("zweistein", "sad"), "why tf did u give us okarun's balls"),
                        (
                            0,
                            "its gonna take me years to castrate someone with no balls so take this and leave",
                        ),
                        (("sawman", "ono"), "..."),
                        (("sawman", "sad"), "jesus"),
                    ],
                ],
            ),
            Obj(
                f"{cwd}/rooms/flichroom/objects/basement.png",
                (205, 465),
                [{("Sigil of Friendship", -1): 3}],
                [
                    [
                        (("sawman", "ono"), "NO WAY?!?!?!?"),
                        (("zweistein", "sad"), "is that the michael bed"),
                        (
                            0,
                            "ihaveseencrimesbeyondanyonespossibilitieswithinthesewalls",
                        ),
                        (
                            ("sawman", "woe"),
                            "...",
                        ),
                        (
                            ("zweistein", "sad"),
                            "skill issue",
                        ),
                    ],
                    [
                        (("zweistein", "sad"), "why tf did u give us okarun's balls"),
                        (
                            0,
                            "its gonna take me years to castrate someone with no balls so take this and leave",
                        ),
                        (("sawman", "ono"), "..."),
                        (("sawman", "sad"), "jesus"),
                    ],
                ],
            ),
        ],
        [
            Portal((993.5, 530.0), (207, 144), 2, (274, 208)),
            Portal((509.5, 473.5), (153, 105), 1, (825.0, 369.0)),
        ],
        [
            (("sawman", "sad"), "god damm that was a terrible sleep"),
            (("sawman", "hapi"), "time to get back on the youtube grindset"),
        ],
    ),
    Room(
        "gaming",
        "I_forgor_my_wallet",
        1,
        [
            Obj(
                f"{cwd}/rooms/gaming/objects/computer.png",
                (947, 313),
                [{("Sigil of Dormancy", -1): 3}],
                [
                    [
                        (("sawman", "ono"), "my beautiful body pillow"),
                        (
                            ("sawman", "woe"),
                            "my girlfried isnt a lot to touch her",
                        ),
                    ],
                ],
            ),
            Obj(
                f"{cwd}/rooms/gaming/objects/gf.png",
                (326, 260),
                [{("Sigil of Friendship", -1): 3}],
                [
                    [
                        (("sawman", "ono"), "NO WAY?!?!?!?"),
                        (("zweistein", "sad"), "is that the michael bed"),
                        (
                            0,
                            "ihaveseencrimesbeyondanyonespossibilitieswithinthesewalls",
                        ),
                        (
                            ("sawman", "woe"),
                            "...",
                        ),
                        (
                            ("zweistein", "sad"),
                            "skill issue",
                        ),
                    ],
                    [
                        (("zweistein", "sad"), "why tf did u give us okarun's balls"),
                        (
                            0,
                            "its gonna take me years to castrate someone with no balls so take this and leave",
                        ),
                        (("sawman", "ono"), "..."),
                        (("sawman", "sad"), "jesus"),
                    ],
                ],
            ),
            Obj(
                f"{cwd}/rooms/gaming/objects/fire.png",
                (0, 225),
                [{("Sigil of Friendship", -1): 3}],
                [
                    [
                        (("sawman", "ono"), "NO WAY?!?!?!?"),
                        (("zweistein", "sad"), "is that the michael bed"),
                        (
                            0,
                            "ihaveseencrimesbeyondanyonespossibilitieswithinthesewalls",
                        ),
                        (
                            ("sawman", "woe"),
                            "...",
                        ),
                        (
                            ("zweistein", "sad"),
                            "skill issue",
                        ),
                    ],
                    [
                        (("zweistein", "sad"), "why tf did u give us okarun's balls"),
                        (
                            0,
                            "its gonna take me years to castrate someone with no balls so take this and leave",
                        ),
                        (("sawman", "ono"), "..."),
                        (("sawman", "sad"), "jesus"),
                    ],
                ],
            ),
        ],
        [
            Portal((825.0, 369.0), (98, 100), 0, (509.5, 473.5)),
        ],
        "",
    ),
]
