Kakao.init("7d2565115739c70be1903fea71d797fb");
// 배포할때에는
// http://www.parkgolfone.com/ 을 대신 url 에 넣기 http://127.0.0.1:8000/ 대신


console.log("thumbnailURL : ", thumbnailUrl)


//점수 공유
function shareKakaoScore() {
  const scoreAreas = document.querySelectorAll(".scoreArea");

  let scores = [];
  scoreAreas.forEach((event) => {
    scores.push(event.outerText);
  });

  Kakao.Share.createDefaultButton({
    container: "#kakaotalk-sharing-btn",
    objectType: "feed",
    content: {
      title: "점수",
      description: "나의 점수 공유!",
      imageUrl: 'thumbnailUrl',
      link: {
        mobileWebUrl: `http://127.0.0.1:8000/score/score_detail/${sid}/`,
        webUrl: `http://127.0.0.1:8000/score/score_detail/${sid}/`,
      },
    },
    buttons: [
      {
        title: "점수 보러가기~!!",
        link: {
          mobileWebUrl: `http://127.0.0.1:8000/score/score_detail/${sid}/`,
          webUrl: `http://127.0.0.1:8000/score/score_detail/${sid}/`,
        },
      },
    ],
  });
}

// 게시글 공유
function shareKakaoPost() {

  const post_title = document.querySelector(".post-detail-title").innerHTML
  console.log("pid = ", pid);

  Kakao.Share.createDefaultButton({
    container: "#kakaotalk-sharing-btn",
    objectType: "feed",
    content: {
      title: post_title,
      description: "재미있는 글을 찾았는데.... 보실래요?",
      imageUrl: "thumbnailUrl",
      link: {
        mobileWebUrl: `http://127.0.0.1:8000/communitys/${bid}/main/${pid}/`,
        webUrl: `http://127.0.0.1:8000/communitys/${bid}/main/${pid}/`,
      },
    },
    buttons: [
      {
        title: "게시글 보러가기~!!",
        link: {
          mobileWebUrl: `http://127.0.0.1:8000/communitys/${bid}/main/${pid}/`,
          webUrl: `http://127.0.0.1:8000/communitys/${bid}/main/${pid}/`,
        },
      },
    ],
  });
}

//게임 공유
function shareKakaoGame(gid) {


  Kakao.Share.createDefaultButton({
    container: "#kakaotalk-sharing-btn",
    objectType: "feed",
    content: {
      title: "점수",
      description: "나의 점수 공유!",
      imageUrl: "thumbnailUrl",
      link: {
        mobileWebUrl: `http://127.0.0.1:8000/score/score_detail/${sid}/`,
        webUrl: `http://127.0.0.1:8000/score/score_detail/${sid}/`,
      },
    },
    buttons: [
      {
        title: "점수 보러가기~!!",
        link: {
          mobileWebUrl: `http://127.0.0.1:8000/score/score_detail/${sid}/`,
          webUrl: `http://127.0.0.1:8000/score/score_detail/${sid}/`,
        },
      },
    ],
  });
}

//장소 공유
function shareKakaoLocation() {
  
  Kakao.Share.createDefaultButton({
    container: "#kakaotalk-sharing-btn",
    objectType: "feed",
    content: {
      title: document.querySelector(".golf-name").innerHTML,
      description: "이 골프장은 어때~?",
      imageUrl: "thumbnailUrl",
      link: {
        mobileWebUrl: `http://127.0.0.1:8000/locations/detail/${ground_id}/`,
        webUrl: `http://127.0.0.1:8000/locations/detail/${ground_id}/`,
      },
    },
    buttons: [
      {
        title: "상세 정보 보러가기",
        link: {
          mobileWebUrl: `http://127.0.0.1:8000/locations/detail/${ground_id}/`,
          webUrl: `http://127.0.0.1:8000/locations/detail/${ground_id}/`,
        },
      },
    ],
  });
}


